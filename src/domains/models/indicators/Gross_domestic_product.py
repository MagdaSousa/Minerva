from src.common.Enums import TablesNames
from pydantic import validator
from src.domains import Column, Integer, String, relationship, ForeignKey, Float, DATE, Base


class GrossDomesticProduct(Base):
    __tablename__ = TablesNames.gross_domestic_product.value

    GDPGrowthAnnualID = Column(Integer, primary_key=True)
    ValueperPeriod = Column(Float(), nullable=False)
    reference_year = Column(DATE(), nullable=False)
    gdp_external_id = Column(String(100), nullable=False)

    country_id = Column(Integer, ForeignKey("CountryIndicators.CountryID"), nullable=False)
    indicator_id = Column(Integer, ForeignKey("PeriodIndicators.IndicatorID"), nullable=False)
    period_id = Column(Integer, ForeignKey("PeriodIndicators.PeriodID"), nullable=False)

    period = relationship(
        "PeriodIndicators", back_populates="GrossDomesticProduct", cascade="all, delete-orphan")
    indicator = relationship(
        "PeriodIndicators", back_populates="GrossDomesticProduct", cascade="all, delete-orphan")
    country = relationship(
        "CountryIndicators", back_populates="GrossDomesticProduct", cascade="all, delete-orphan")

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
               f" gdp_external_id={self.gdp_external_id!r}," \
               f" country_id={self.country_id!r}," \
               f" period_id={self.period_id!r}," \
               f" indicator_id={self.indicator_id!r})"
