from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from src.database.database import ForeignKey, Column, Base


class Association(Base):
    __tablename__ = "Association"
    id = Column(Integer, primary_key=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey("Country.id"), nullable=False)
    indicators_id = Column(Integer, ForeignKey("Indicators.id"), nullable=False)

    gdp_association_fk = relationship("GrossDomesticProduct", back_populates="association_gdp_fk")
