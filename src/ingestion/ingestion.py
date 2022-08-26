from loguru import logger

from src.database.database import DBConnection, insert
from src.domains.models.association_tables.association_tables import Association
from src.domains.models.country.country import Country
from src.domains.models.country.region import Region
from src.domains.models.income_groups.invome_groups import IncomeGroups
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from src.domains.models.indicators.indicators import Indicators
from src.domains.models.period.period import Period


class IngestionInPostgres:
    def __init__(self , df_merge,db:DBConnection):
        self.df_merge = df_merge
        self.insert = insert
        self.db = db
        self.engine = self.db.engine
        self.regions = self.df_merge.drop_duplicates(subset=['Region'])
        self.income_groups = self.df_merge.drop_duplicates(subset=['IncomeGroup'])
        self.indicators = self.df_merge[['Indicator Name', 'Indicator Code']].drop_duplicates()
        self.period_list = {}

    def delete_date(self):

        self.db.delete_executor(GrossDomesticProduct)
        self.db.delete_executor(Association)
        self.db.delete_executor(Country)
        self.db.delete_executor(Region)
        self.db.delete_executor(Period)
        self.db.delete_executor(Indicators)
        self.db.delete_executor(IncomeGroups)

    def ingestion_data_in_imutable_data(self):
        index = 1
        self.ingestion_period_table_bach(index)
        self.ingestion_region_table_bach(index)
        self.ingestion_income_groups_table_bach(index)
        self.ingestion_indicator_table_bach(index)

    def iterate_in_rows_to_ingestion(self):
        try:
            self.delete_date()
            self.ingestion_data_in_imutable_data()
            for index, row in self.df_merge.iterrows():
                count = index + 1

                self.ingestion_country_table_bach(row, count)
                self.ingestion_association_groups_table_bach(row, count)
                self.ingestion_gdp_table_bach(row, count)

        except Exception as error:
            raise logger.error(f"[iterate_in_rows_to_ingestion] - ERROR - verificar ingestion {error}")

    def ingestion_period_table_bach(self, pk):

        for column in list(self.df_merge.columns):
            if column.isnumeric() and not None:
                self.db.insert_executor(Period, {"id": pk, "research_year": int(column)})
                self.period_list[column] = pk
                pk += 1

    def ingestion_country_table_bach(self, row, pk):

        self.db.insert_executor(Country, {"id": pk,
                                          "country_name": row['Country Name'],
                                          "country_code": row['Country Code'],
                                          "region_id": row['RegionId'],
                                          "income_group_id": row['IncomeGroupsId']
                                          })

    def ingestion_region_table_bach(self, pk):

        self.regions['Region'].fillna('inexistente', inplace=True)
        self.df_merge['Region'].fillna('inexistente', inplace=True)
        key = pk
        for index, region_name in self.regions['Region'].items():
            self.db.insert_executor(Region, {"id": key, "region_name": region_name})
            self.df_merge.loc[self.df_merge['Region'] == region_name, 'RegionId'] = key

            key += 1

    def ingestion_gdp_table_bach(self, row, pk):
        for column in list(self.df_merge.columns):
            if column.isnumeric() and not None:
                self.db.insert_executor(GrossDomesticProduct, {
                    "value_per_period": row[column],
                    "association_id": pk,
                    "period_id": self.period_list[column]})

    def ingestion_indicator_table_bach(self, pk):
        self.df_merge['Indicator Name'].fillna('inexistente', inplace=True)
        key = pk
        for index, indicators in self.indicators.iterrows():
            self.db.insert_executor(Indicators, {"id": key,
                                                 "indicator_name": indicators['Indicator Name'],
                                                 "indicator_code": indicators['Indicator Code']})
            self.df_merge.loc[self.df_merge['Indicator Name'] == indicators['Indicator Name'], 'IndicatorsId'] = key
            key += 1

    def ingestion_income_groups_table_bach(self, pk):

        self.income_groups['IncomeGroup'].fillna('inexistente', inplace=True)
        self.df_merge['IncomeGroup'].fillna('inexistente', inplace=True)
        key = pk
        for index, income_groups in self.income_groups['IncomeGroup'].items():
            self.db.insert_executor(IncomeGroups, {"id": key,
                                                   "income_level": income_groups})
            self.df_merge.loc[self.df_merge['IncomeGroup'] == income_groups, 'IncomeGroupsId'] = key
            key += 1

    def ingestion_association_groups_table_bach(self, row, pk):

        self.db.insert_executor(Association, {"id": pk,
                                              "country_id": pk,
                                              "indicators_id": row['IndicatorsId']})
