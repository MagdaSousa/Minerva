import re
from src.database.database import DBConnection, insert
from src.domains.models.country.country import Country
from src.domains.models.country.region import Region
from src.domains.models.income_groups.invome_groups import IncomeGroups
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from src.domains.models.indicators.indicators import Indicators
from src.domains.models.period.period import Period

import pandas as pd
from typing import Union
import operator
from loguru import logger


class ExtractAndTransformDataSet:
    def __init__(self):
        self.url_gist_country = 'https://gist.githubusercontent.com/MagdaSousa/da6d007edfdf38019b0de219c4d18ad6/raw' \
                                '/a5f33797ec661a77d3587352f699dbb97b3487d8/API_NY_GDP_MKT_KD_ZG_DS2_en_csv_v2_4344066' \
                                '.csv '
        self.url_gist_region = 'https://gist.githubusercontent.com/MagdaSousa/46c3139e06d45f22b28b9f0c1a9d1df2/raw' \
                               '/98c2030cea6d5a66fdda1f2f86467999b73f7b93' \
                               '/Metadata_Country_API_NY_GDP_MKTP_KD_ZG_DS2_en_csv_v2_4344066.csv '

    def read_datasets(self, url: str):
        """
        FAz a leitura do csv transformando em dataframe
        :param url:
        :return:
        """
        try:

            logger.info("[read_datasets] - load data")
            return pd.read_csv(url)

        except Exception as err:
            raise logger.error(f"[read_datasets] -ERROR- Verify load data {err}")

    def verify_shape(self, df, df2) -> Union[tuple, tuple]:
        """
        verificação necessária para analisar se é viavel o merge entre os datasets
        :return:
        """
        try:

            logger.info("[verify_shape] - load data")
            return df.shape, df2.shape

        except Exception as err:
            raise logger.error(f"[verify_shape] -ERROR- Verify  {err}")

    def verify_duplicate_columns(self, df_indicator, df_region) -> list:
        """
        Verifica sehá colunas iguais entre os datasets, e extrai essas colunas para que eu consiga fazer o merge entre elas
        :param df_indicator:
        :param df_region:
        :return:
        """
        try:
            logger.info("[verify_duplicate_columns] - load data")
            list_columns = operator.add(list(df_region.columns.values), list(df_indicator.columns.values))
            duplicates = [x for x in list_columns if list_columns.count(x) > 1]
            print(duplicates)
            return duplicates

        except Exception as err:
            raise logger.error(f"[verify_duplicate_columns] -ERROR- Verify  {err}")

    def merge_dataframes(self, df_indicator, df_region, list_duplicates_columns):
        """
        :param df_indicator:
        :param df_region:
        :return:
        """
        try:
            logger.info("[merge_dataframes] - load data")

            df_region.rename(columns={'TableName': 'Country Name'}, inplace=True)

            outer_merged = pd.merge(
                df_indicator, df_region, how="left", on='Country Name')
            return outer_merged

        except Exception as err:
            raise logger.error(f"[verify_shape] -ERROR- Verify  {err}")

    def include_external_ids(self, country_code):
        """
        Recebe um country_code e cria um código externo de referencia para o atual,
         que será usado para que as consultas sejam mais ágeis
        :param country_code:
        :return:
        """
        try:
            list_ascii = [str(ord(x)) for x in country_code]
            country_external_id = int("".join(list_ascii))
            return country_external_id

        except Exception as err:
            raise logger.error(f"[verify_shape] -ERROR- Verify  {err}")

    def execute_trasform(self):
        try:
            df_region = self.read_datasets(self.url_gist_region)
            df_indicators = self.read_datasets(self.url_gist_country)
            self.verify_shape(df_region, df_indicators)
            list_duplicates_columns = self.verify_duplicate_columns(df_indicators, df_region)
            # merge
            merge_dataframes = self.merge_dataframes(df_indicators, df_region, list_duplicates_columns)

            # drop uplicates and verify

            self.compare_records_from_country_name_columns(merge_dataframes)
            df_new_instance = self.delete_columns(merge_dataframes)

            return self.verify_nan_values(df_new_instance)


        except Exception as err:
            raise logger.error(f"[verify_shape] -ERROR- Verify  {err}")

    def compare_records_from_country_name_columns(self, df):
        """
        Verificando se o merge foi executado corretamente,
         comparando os valores das colunas com o mesmo nome, caso esteja certo, posso eleiminar a redundancia
        :param df:
        :return:
        """
        try:

            assert list(df['Country Code_x'].values) == list(df['Country Code_x'].values)
        except AssertionError as err:
            raise logger.error(f"[compare_records_from_country_name_columns] -ERROR- Verificar o merge, não esstá "
                               f"adequado  {err}")

    def delete_columns(self, df):
        df.drop(columns=['Unnamed: 5', 'Country Code_x', 'Unnamed: 66'], inplace=True)
        df.rename(columns={'Country Code_y': 'Country Code'}, inplace=True)
        print("kkk", df.columns.values)
        return df

    def verify_nan_values(self, df):
        for columns in list(df.columns.values):
            check_for_nan = df[columns].isnull().values.any()
            if check_for_nan:
                if isinstance(df[columns][0], str):
                    df.fillna("sem item cadastrado")
                else:
                    df.fillna(0)

        return df

    def processamento_para_database(self):
        """
        criando ids externos para facilitar as consultas
        :return:
        """
        df_merge = self.execute_trasform()
        return df_merge


class IngestionInPostgres:
    def __init__(self, df_merge):
        self.df_merge = df_merge
        self.insert = insert
        self.db = DBConnection()
        self.engine = self.db.engine

    def iterate_in_rows_to_ingestion(self):
        try:
            for index, row in self.df_merge.iterrows():
                index = +1
                self.ingestion_period_table_bach(index)
                # self.ingestion_region_table_bach(row)
                # self.ingestion_gdp_table_bach(row)
                # self.ingestion_indicator_table_bach(row)
                # self.ingestion_country_table_bach(row)
                # self.ingestion_income_groups_table_bach(row)

        except Exception as error:
            raise logger.error(f"[iterate_in_rows_to_ingestion] - ERROR - verificar ingestion {error}")

    def ingestion_period_table_bach(self, pk):

        for column in list(self.df_merge.columns):
            if column.isnumeric():
                self.db.insert_executor(Period, {"id": pk, "research_year": int(column)})

    def ingestion_country_table_bach(self, row, pk):

        self.db.insert_executor(Country, {"id": pk,
                                          "country_name": row[''],
                                          "country_code": row[''],
                                          "region_id": row[''],
                                          "income_group_id": row[''],
                                          "region_country_fk": row[''],
                                          "income_country_fk": row[''],
                                          "indicator_country_fk": row[''],
                                          })

    def ingestion_region_table_bach(self, row,pk):
        self.db.insert_executor(Region, {"id": pk,
                                          "region_name": row[''],
                                          "country_region_fk": row[''])

    def ingestion_gdp_table_bach(self, row,pk):
        self.db.insert_executor(GrossDomesticProduct, {"id": pk,
                                          "value_per_period": row[''],
                                          "association_id": row[''],
                                          "period_id": row[''],
                                          "income_group_id": row[''],
                                          "gdp_period_fk": row[''],
                                          "association_gdp_fk": row['']})

    def ingestion_indicator_table_bach(self, row,pk):

        self.db.insert_executor(Indicators, {"id": pk,
                                           "indicator_name": row[''],
                                           "indicator_code": row[''],
                                           "country_indicators_fk": row['']})

    def ingestion_income_groups_table_bach(self, row):

        IncomeGroups(
            indicator_name=row['income_level'])

    def ingestion_association_groups_table_bach(self, row):

        IncomeGroups(
            indicator_name=row['income_level'])


teste = ExtractAndTransformDataSet().processamento_para_database()

ingestion = IngestionInPostgres(teste)
ingestion.iterate_in_rows_to_ingestion()
