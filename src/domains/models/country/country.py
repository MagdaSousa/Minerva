from src.common.Enums import TablesNames
from pydantic import validator
from src.database.database import Base, Column, Integer, String, relationship, ForeignKey
from src.domains.models.association_tables.association_tables import Association

class Country(Base):
    __tablename__ = TablesNames.country.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100), nullable=False)
    country_code = Column(String(50), nullable=False)
    region_id = Column(Integer, ForeignKey("Region.id"), nullable=False)
    income_group_id = Column(Integer, ForeignKey("IncomeGroups.id"), nullable=False)

    region_country_fk = relationship("Region", back_populates="country_region_fk")
    income_country_fk = relationship("IncomeGroups", back_populates="country_income_fk")
    indicator_country_fk = relationship(
        "Indicators", secondary="Association", back_populates="country_indicators_fk"
    )

    @validator('country_name')
    def field_country_name_cannot_be_null(cls, country_name):
        if not country_name.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    @validator('country_code')
    def field_reference_year_cannot_be_null(cls, country_code):
        if not country_code.replace(" ", ""):
            raise ValueError('field country_code cannot be null')

    def __repr__(self):
        return f"Country(id={self.id!r}, " \
               f" country_name={self.country_name!r}," \
               f" country_code={self.country_code!r})"
