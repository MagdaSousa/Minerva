from src.common.Enums import TablesNames
from src.database.database import Base, Column, Integer, String, relationship
from pydantic import validator
from src.domains.models.association_tables.association_tables import indicators_period_association_table,\
    country_indicator_association_table


class Indicators(Base):
    __tablename__ = TablesNames.indicators.value

    indicatorID = Column(Integer, primary_key=True)
    indicator_name = Column(String(50), nullable=False)
    indicator_code = Column(String(50), nullable=False)

    #associative table many-to-many
    period = relationship(
        "period", secondary=indicators_period_association_table, back_populates=f"{TablesNames.indicators.value}"
    )

    country = relationship(
        "country", secondary=country_indicator_association_table, back_populates=f"{TablesNames.indicators.value}"
    )

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
