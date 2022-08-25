import math
import numpy as np
from pydantic import BaseModel

from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct


# Actions
class GDPResponseSchema:
    def __init__(self, data):
        self.data = data

    def assemble_the_schematic_for_the_indicator(self):
        dict_values_indicators = {}

        gdp = self.data[0]
        country = self.data[1]
        indicators = self.data[2]
        income_groups = self.data[3]
        for fields in gdp:

            if str(fields.value_per_period) == 'nan':
                values_per_period = 0
            else:
                values_per_period = round(fields.value_per_period, 2)
            dict_values_indicators[fields.gdp_period_fk.research_year] = values_per_period

        return {"country_name": country.country_name,
                "country_code": country.country_code,
                "income_groups": income_groups.country_code,
                "region_name": country.region_country_fk.region_name,
                "indicator_name": indicators[0].indicator_name,
                "list_values_indicators": [dict_values_indicators]}


class GrossRateResponseSchema:
    def __init__(self, data):
        self.data = data

    def formatting_growth_rate_data_by_country(self):
        dict_values_indicators = {}

        gdp = self.data[0]
        country = self.data[1]
        for fields in gdp:

            if str(fields.value_per_period) == 'nan':
                values_per_period = 0
            else:
                values_per_period = round(fields.value_per_period, 2)
            dict_values_indicators[fields.gdp_period_fk.research_year] = f"{round(values_per_period)} %"

        return {"country_name": country.country_name,
                "country_code": country.country_code,
                "GDP growth annual %": [dict_values_indicators]}


class GDPResponseSchema2(BaseModel):
    country_name: str
    country_code: str
    region_name: str
    indicator_name: str
    list_values_indicators: list


class GDPCountryNameSchema(BaseModel):
    country_name: str
    country_code: str
    region_name: str


class GDPInfosSchema(BaseModel):
    id: int
    value_per_period: float
    association_id: int
    period_id: int


class GDPFromRegion(BaseModel):
    gdp_external_id: str
    country_name: int
    value: float


class GDPFromPeriod(BaseModel):
    gdp_external_id: str
    country_name: int
    value: float
