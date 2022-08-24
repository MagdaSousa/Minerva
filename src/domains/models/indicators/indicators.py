from src.common.Enums import TablesNames
from src.database.database import Base, Column, Integer, String, relationship
from pydantic import validator

from src.domains.models.association_tables.association_tables import Association


class Indicators(Base):
    __tablename__ = TablesNames.indicators.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    indicator_name = Column(String(50), nullable=False)
    indicator_code = Column(String(50), nullable=False)
    country_indicators_fk = relationship(
        "Country", secondary="Association", back_populates="indicator_country_fk"
    )

    @validator('indicator_name')
    def field_country_name_cannot_be_null(cls, indicator_name):
        if not indicator_name.replace(" ", ""):
            raise ValueError('field indicator_name cannot be null')

    @validator('indicator_code')
    def field_country_code_cannot_be_null(cls, indicator_code):
        if not indicator_code.replace(" ", ""):
            raise ValueError('field indicator_code cannot be null')

    def __repr__(self):
        return f" Indicators(id={self.id!r}, " \
               f" indicator_name={self.indicator_name!r}," \
               f" indicator_code={self.indicator_code!r})"
