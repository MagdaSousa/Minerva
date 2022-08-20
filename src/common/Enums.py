from enum import Enum


class TablesNames(Enum):
    database = "db_minerva"
    indicators = f"{database}.Indicators"
    country = f"{database}.Country"
    region = f"{database}.Region"
    period = f"{database}.Period"
    income_groups = f"{database}.IncomeGroups"
    gross_domestic_product = f"{database}.GrossDomesticProduct"
