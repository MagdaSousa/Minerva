from src.common.Enums import TablesNames
from src.domains import Base, Column, Integer, String, relationship
from pydantic import validator


class Indicator(Base):
    __tablename__ = TablesNames.indicators.value

    indicatorID = Column(Integer, primary_key=True)
    indicator_name = Column(String(50), nullable=False)
    indicator_code = Column(String(50), nullable=False)
    gdp = relationship("GrossDomesticProduct", back_populates="indicator")

    @validator('indicator_name')
    def field_country_name_cannot_be_null(cls, indicator_name):
        if not indicator_name.replace(" ", ""):
            raise ValueError('field indicator_name cannot be null')

    @validator('indicator_code')
    def field_country_name_cannot_be_null(cls, indicator_code):
        if not indicator_code.replace(" ", ""):
            raise ValueError('field indicator_code cannot be null')

    def __repr__(self):
        return f" Indicator(indicatorID={self.indicatorID!r}, " \
               f" indicator_name={self.value!r}," \
               f" indicator_code={self.growth_average!r})"
