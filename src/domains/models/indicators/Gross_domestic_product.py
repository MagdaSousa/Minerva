from src.common.Enums import TablesNames
from pydantic import validator
from src.database.database import Base, Column, Integer, ForeignKey, Float, DATE


class GrossDomesticProduct(Base):
    __tablename__ = TablesNames.gross_domestic_product.value

    GDPGrowthAnnualID = Column(Integer, primary_key=True)
    ValueperPeriod = Column(Float(), nullable=False)
    reference_year = Column(DATE(), nullable=False)
    # gdp_external_id = Column(String(100), nullable=False)

    #country_indicator = Column(Integer, ForeignKey("country_indicator.Indicators"), nullable=False)
    #indicators_period = Column(Integer, ForeignKey("indicators_period.Indicators"), nullable=False)

    @validator('ValueperPeriod')
    def field_value_cannot_be_null(cls, value):
        if not value.replace(" ", ""):
            raise ValueError('field value cannot be null')

    @validator('reference_year')
    def field_reference_year_cannot_be_null(cls, reference_year):
        if not reference_year.replace(" ", ""):
            raise ValueError('field reference year cannot be null')

    @validator('growth_average')
    def field_growth_average_cannot_be_null(cls, growth_average):
        if not growth_average.replace(" ", ""):
            raise ValueError('field growth average cannot be null')

    @validator('growth_rate')
    def field_growth_rate_cannot_be_null(cls, growth_rate):
        if not growth_rate.replace(" ", ""):
            raise ValueError('field growth rate cannot be null')

    def __repr__(self):
        return f" GrossDomesticProduct(GrossDomesticProductID={self.GrossDomesticProductID!r}, " \
               f" ValueperPeriod={self.ValueperPeriod!r}," \
               f" reference_year={self.reference_year!r}," \
               f" country_indicator={self.country_indicator!r}," \
               f" indicators_period={self.country_id!r}"
