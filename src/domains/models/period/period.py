from src.common.Enums import TablesNames
from pydantic import validator
from src.database.database import Base, Column, Integer, String, relationship


# from src.domains.models.association_tables.association_tables import indicators_period_association_table


class Period(Base):
    __tablename__ = TablesNames.period.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    research_year = Column(Integer, nullable=False)
    period_gdp_fk = relationship("GrossDomesticProduct", back_populates="gdp_period_fk")

    @validator('research_year')
    def field_reference_year_cannot_be_null(cls, country_code):
        if not country_code.replace(" ", ""):
            raise ValueError('field country_code cannot be null')

    def __repr__(self):
        return f"Period(id={self.id!r},  research_year={self.research_year!r})"
