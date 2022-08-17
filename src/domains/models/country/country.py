from src.common.Enums import TablesNames
from pydantic import validator
from src.domains import Base, Column, Integer, String, relationship, ForeignKey


class Country(Base):
    __tablename__ = TablesNames.country.value

    countryID = Column(Integer, primary_key=True)
    country_name = Column(String(50), nullable=False)
    country_code = Column(String(50), nullable=False)
    region_id = Column(Integer, ForeignKey("Region.id"), nullable=False)
    gdp = relationship("GrossDomesticProduct", back_populates="country")
    country = relationship("Region", back_populates="country")

    @validator('country_name')
    def field_country_name_cannot_be_null(cls, country_name):
        if not country_name.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    @validator('country_code')
    def field_reference_year_cannot_be_null(cls, country_code):
        if not country_code.replace(" ", ""):
            raise ValueError('field country_code cannot be null')

    def __repr__(self):
        return f"Country(countryID={self.countryID!r}, " \
               f" country_name={self.country_name!r}," \
               f" country_code={self.country_code!r}," \
               f" region_id={self.country_code!r} )"
