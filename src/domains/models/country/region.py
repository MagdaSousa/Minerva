from sqlalchemy import ForeignKey

from src.common.Enums import TablesNames
from src.database.database import Base, Column, Integer, String, relationship, ForeignKey
from pydantic import validator


class Region(Base):
    __tablename__ = TablesNames.region.value

    RegionID = Column(Integer, primary_key=True)
    RegionName = Column(String(50), nullable=False)
    IncomeGroupID = Column(Integer, ForeignKey("incomegroups.IncomeGroupID"), nullable=False)

    # many-to-one
    income_group = relationship("IncomeGroups", back_populates=f"{TablesNames.region.value.lower()}")
    # one-to-one
    country = relationship("Country", back_populates=f"{TablesNames.region.value.lower()}", uselist=False)



    @validator('region_name')
    def field_country_name_cannot_be_null(cls, region_name):
        if not region_name.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    def __repr__(self):
        return f"Region(RegionID={self.RegionID!r}, " \
               f" RegionName={self.RegionName!r}," \
               f" IncomeGroupID={self.IncomeGroupID!r},"

