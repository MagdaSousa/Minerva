from datetime import datetime
from pydantic import BaseModel


class GDPCountryNameSchema(BaseModel):
    gdp_external_id: str
    value: int
    growth_average: float
    growth_rate: float
    reference_year: datetime


class GDPFromRegion(BaseModel):
    gdp_external_id: str
    country_name: int
    value: float


class GDPFromPeriod(BaseModel):
    gdp_external_id: str
    country_name: int
    value: float
