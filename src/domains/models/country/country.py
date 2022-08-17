from src.common.Enums import TablesNames
from src.domains import Base, Column, Integer, String, relationship, ForeignKey


class Country(Base):
    __tablename__ = TablesNames.country.value

    countryID = Column(Integer, primary_key=True)
    country_name = Column(String(50), nullable=False)
    country_code = Column(String(50), nullable=False)
    region_id = Column(Integer, ForeignKey("Region.id"), nullable=False)
    gdp = relationship("GrossDomesticProduct", back_populates="country")
    country = relationship("Region", back_populates="country")

    def __repr__(self):
        return f"Country(countryID={self.countryID!r}, " \
               f" country_name={self.country_name!r}," \
               f" country_code={self.country_code!r}," \
               f" region_id={self.country_code!r} )"

