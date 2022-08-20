from src.common.Enums import TablesNames
from pydantic import validator
from src.domains import Base, Column, Integer, String, relationship, ForeignKey


class Country(Base):
    __tablename__ = TablesNames.country.value

    CountryID = Column(Integer, primary_key=True)
    CountryName = Column(String(50), nullable=False)
    CountryCode = Column(String(50), nullable=False)
    IncomeGroupID = Column(Integer, ForeignKey("Region.id"), nullable=False)

    gdp = relationship("GrossDomesticProduct", back_populates="country")
    country = relationship("Region", back_populates="country")

    @validator('CountryName')
    def field_country_name_cannot_be_null(cls, country_name):
        if not country_name.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    @validator('CountryCode')
    def field_reference_year_cannot_be_null(cls, country_code):
        if not country_code.replace(" ", ""):
            raise ValueError('field country_code cannot be null')

    def __repr__(self):
        return f"Country(CountryID={self.countryID!r}, " \
               f" country_name={self.country_name!r}," \
               f" CountryCode={self.country_code!r}," \
               f" IncomeGroupID={self.country_code!r} )"

