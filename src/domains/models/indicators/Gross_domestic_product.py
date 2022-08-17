from src.common.Enums import TablesNames
from pydantic import validator
from src.domains import Column, Integer, String, relationship, ForeignKey, Float, DATE, Base


class GrossDomesticProduct(Base):
    __tablename__ = TablesNames.gross_domestic_product.value

    GrossDomesticProductID = Column(Integer, primary_key=True)
    value = Column(Float(), nullable=False)
    growth_average = Column(Float(), nullable=False)
    growth_rate = Column(Float(), nullable=False)
    reference_year = Column(DATE(), nullable=False)
    gdp_external_id = Column(String(100), nullable=False)

    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)
    indicator_id = Column(Integer, ForeignKey("indicator.id"), nullable=False)

    period = relationship(
        "period", back_populates="gdp", cascade="all, delete-orphan")
    indicator = relationship(
        "indicator", back_populates="gdp", cascade="all, delete-orphan")

    @validator('value')
    def field_value_cannot_be_null(cls, value):
        if not value.replace(" ", ""):
            raise ValueError('field value cannot be null')


    @validator('reference_year')
    def field_reference_year_cannot_be_null(cls, v):
        if ' ' not in v:
            raise ValueError('field reference year cannot be null')
        return v.title()

    @validator('growth_average')
    def field_growth_average_cannot_be_null(cls, v):
        if ' ' not in v:
            raise ValueError('field growth average cannot be null')
        return v.title()

    @validator('growth_rate')
    def field_growth_rate_cannot_be_null(cls, v):
        if ' ' not in v:
            raise ValueError('field growth rate cannot be null')
        return v.title()

    def __repr__(self):
        return f" GrossDomesticProduct(GrossDomesticProductID={self.GrossDomesticProductID!r}, " \
               f" value={self.value!r}," \
               f" growth_average={self.growth_average!r}," \
               f" growth_rate={self.growth_rate!r}," \
               f" reference_year={self.reference_year!r}," \
               f" gdp_external_id={self.gdp_external_id!r}," \
               f" country_id={self.country_id!r}," \
               f" indicator_id={self.indicator_id!r})"
