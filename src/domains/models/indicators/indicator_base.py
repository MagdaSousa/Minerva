from src.common.Enums import TablesNames
from src.domains import Base,Column,Integer,String,relationship


class Indicator(Base):
    __tablename__ = TablesNames.indicators.value

    indicatorID = Column(Integer, primary_key=True)
    indicator_name = Column(String(50),nullable=False)
    indicator_code = Column(String(50),nullable=False)
    gdp = relationship("GrossDomesticProduct", back_populates="indicator")

    def __repr__(self):
        return f" Indicator(indicatorID={self.indicatorID!r}, " \
               f" indicator_name={self.value!r}," \
               f" indicator_code={self.growth_average!r})"