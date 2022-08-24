import pytest
from loguru import logger
import pandas as pd
from src.ingestion.ingestion import ExtractAndTransformDataSet

url_gist_country = 'https://gist.githubusercontent.com/MagdaSousa/da6d007edfdf38019b0de219c4d18ad6/raw' \
                   '/a5f33797ec661a77d3587352f699dbb97b3487d8/API_NY_GDP_MKT_KD_ZG_DS2_en_csv_v2_4344066' \
                   '.csv '
url_gist_region = 'https://gist.githubusercontent.com/MagdaSousa/46c3139e06d45f22b28b9f0c1a9d1df2/raw' \
                  '/98c2030cea6d5a66fdda1f2f86467999b73f7b93' \
                  '/Metadata_Country_API_NY_GDP_MKTP_KD_ZG_DS2_en_csv_v2_4344066.csv '


class TestExtractAndTransformDataSet():
    extract_base = ExtractAndTransformDataSet()
    df_gist_country = pd.read_csv(url_gist_country)
    df_gist_region = pd.read_csv(url_gist_country)

    def test_validade_shape(self):
        shape = self.extract_base.verify_shape(self.df_gist_country, self.df_gist_region)
        assert shape == (self.df_gist_country.shape, self.df_gist_region.shape)

    def test_should_return_duplicate_values(self):
        self.extract_base.verify_duplicate_columns(df_indicator, df_region)

    def test_must_perform_the_merge_between_the_dataframes(self):
        self.extract_base.merge_dataframes(df_indicator,
                                           df_region,
                                           list_duplicates_columns)

    def test_should_return_a_single_dataframe_with_no_duplicate_columns(self):
        self.extract_base.execute_trasform(self)


class TestIngestionInPostgres:

    def test_must_create_the_object_only_from_the_numerical_data(self):
        self.extract_base.ingestion_period_table_bach(self)


