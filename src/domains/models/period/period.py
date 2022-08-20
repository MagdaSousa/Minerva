from src.common.Enums import TablesNames
from pydantic import validator
from src.domains import Base, Column, Integer, String, relationship, ForeignKey


class Period(Base):
    __tablename__ = TablesNames.period.value

    PeriodID = Column(Integer, primary_key=True)
    ResearchYear = Column(String(50), nullable=False)

    @validator('PeriodID')
    def field_country_name_cannot_be_null(cls, country_name):
        if not country_name.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    @validator('ResearchYear')
    def field_reference_year_cannot_be_null(cls, country_code):
        if not country_code.replace(" ", ""):
            raise ValueError('field country_code cannot be null')

    def __repr__(self):
        return f"Period(PeriodID={self.countryID!r},  ResearchYear={self.ResearchYear!r})"