from sqlalchemy.orm import relationship

from src.common.Enums import TablesNames
from pydantic import validator
from src.database.database import Base, Column, Integer, ForeignKey, Float, DATE


class GrossDomesticProduct(Base):
    __tablename__ = TablesNames.gross_domestic_product.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    value_per_period = Column(Float(), nullable=False)
    association_id = Column(Integer, ForeignKey("Association.id"), nullable=False)
    period_id = Column(Integer, ForeignKey("Period.id"), nullable=False)

    gdp_period_fk = relationship("Period", back_populates="period_gdp_fk")
    association_gdp_fk = relationship("Association", back_populates="gdp_association_fk")

    @validator('value_per_period')
    def field_value_cannot_be_null(self, value):
        if not value.replace(" ", ""):
            raise ValueError('field value cannot be null')

    def __repr__(self):
        return f" GrossDomesticProduct(id={self.id!r}, " \
               f" value_per_period={self.value_per_period!r}," \
               f" country_id={self.country_id!r}," \
               f" indicators_id={self.indicators_id!r}," \
               f" period_id={self.period_id!r}"
