from enum import Enum


class TablesNames(Enum):
    database = "db_indicators"
    indicators = f"{database}.Indicators"
    country = f"{database}.Country"
    region = f"{database}.Region"
    gross_domestic_product = f"{database}.GrossDomesticProduct"
