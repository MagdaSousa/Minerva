from src.domains import Column,Integer,String,relationship,ForeignKey
from src.domains.models.indicator.indicator_base import IndicatorBase


class GrossDomesticProduct(IndicatorBase):
    __tablename__ = "GrossDomesticProduct"

    id = Column(Integer, primary_key=True)
    indicator_name = Column(String(50),nullable=False)
    indicator_code = Column(String(50),nullable=False)
    period_id = relationship(
      "´period", back_populates="gdp", cascade="all, delete-orphan")

    def __repr__(self):
       return f"GrossDomesticProduct(id={self.id!r}, " \
              f"indicator_name={self.name!r}," \
              f" indicator_code={self.fullname!r}," \
              f" period_id={self.period_id!r})"


