from src.domains.models.country.country import Country
from src.domains.models.country.region import Region
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from src.domains.models.indicators.indicator_base import Indicator
from src.domains.repository.indicator_repository.cross_domestic_product_repository import GDPRepository
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
            list_columns = operator.add(df_region.columns, df_indicator.columns)
            duplicates = [x for x in list_columns if list_columns.count(x) > 1]
            return duplicates

        except Exception as err:
            raise logger.error(f"[verify_shape] -ERROR- Verify  {err}")

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
                df_indicator, df_region, how="left", on=list_duplicates_columns)
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

            return self.merge_dataframes(df_indicators, df_region, list_duplicates_columns)

        except Exception as err:
            raise logger.error(f"[verify_shape] -ERROR- Verify  {err}")

    def processamento_para_database(self):
        """
        criando ids externos para facilitar as consultas
        :return:
        """
        df_merge = self.execute_trasform()

        df_merge['external_country_id'] = df_merge['Country Code'].map(self.include_external_ids)
        df_merge['external_indicator_id'] = df_merge['Indicator Code'].map(self.include_external_ids)
        df_merge['external_IncomeGroup_id'] = df_merge['IncomeGroup'].map(self.include_external_ids)
        df_merge['external_Region_id'] = df_merge['Region'].map(self.include_external_ids)

        return df_merge



class IngestionInPostgres:
    def __init__(self,df_merge):
        self.df_merge =df_merge

    def iterate_in_rows_to_ingestion(self):
        for index, row in self.df_merge.iterrows():
            row["IncomeGroup"]
            row["Country Code"]
            row["Region"]


    def ingestion_country_table_bach(self,**kwargs):

         country = Country(
             countryID=,
             country_name= ,
             country_code=,
             region_id=  )

    def ingestion_region_table_bach(self,**kwargs):
        region = Region(
               id={},
               regionID={},
               region_name={})


    def ingestion_gdp_table_bach(self,**kwargs):
         GrossDomesticProduct(
             GrossDomesticProductID={},
             value={},
             growth_average={},
             growth_rate={},
             reference_year={},
             gdp_external_id={},
             country_id={},
             indicator_id={})

    def ingestion_indicator_table_bach(self,**kwargs):
        indicator =Indicator(
            indicatorID={},
         indicator_name={},
         indicator_code={})
#
# file_indicator = 'https://gist.githubusercontent.com/MagdaSousa/da6d007edfdf38019b0de219c4d18ad6/raw' \
#                  '/a5f33797ec661a77d3587352f699dbb97b3487d8/API_NY_GDP_MKT_KD_ZG_DS2_en_csv_v2_4344066.csv '
# df_indicator = pd.read_csv(file_indicator)
# print(df_indicator.columns)
#
# file_region = 'https://gist.githubusercontent.com/MagdaSousa/46c3139e06d45f22b28b9f0c1a9d1df2/raw' \
#               '/98c2030cea6d5a66fdda1f2f86467999b73f7b93/Metadata_Country_API_NY_GDP_MKTP_KD_ZG_DS2_en_csv_v2_4344066.csv '
# df_region = pd.read_csv(file_region)
# print(df_region.columns)
# # df_indicator.join(df_region, on='Country Code', how='inner')
#
#
# print(df_region.shape)
# print(df_indicator.shape)
# df_region.rename(columns={'TableName': 'Country Name'}, inplace=True)
#
# outer_merged = pd.merge(
#     df_indicator, df_region, how="left", on=["Country Code", "Country Name"])
# print(outer_merged.shape)
# outer_merged.to_csv("banana.csv")
# class IngestionBatch:
#     def __init__(self, nome, cor):
#        pass
#     def activate_process_batch_ingestion(self):
#         pass
#
#     def ingestion_country_table_bach(self):
#
#          country = Country(
#              countryID=,
#              country_name= ,
#              country_code=,
#              region_id=  )
#
#     def ingestion_country_table_bach(self):
#         region = Region(
#                id={},
#                regionID={},
#                region_name={})
#
#
# class GDPIngestionBatch:
#     """
#     GDP -Gross Domestic Product ingestion
#     """
#
#
#     @staticmethod
#     def ingestion_gross_domestic_product(db: Session, gdp_data) -> GDPRepository:
#         try:
#             verify_period(intial_period, final_period)
#             gdp = GDPRepository.find_gdp_by_region_name(db, intial_period, final_period)
#
#             return gdp
#         except Exception as err:
#             raise logger.error(f"[GDPAction].[find_by_region_name]- ERROR- {err} ")
