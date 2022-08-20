from src.common.Enums import TablesNames
from src.domains import Base, Column, Integer, String, relationship
from pydantic import validator


class Region(Base):
    __tablename__ = TablesNames.region.value

    regionID = Column(Integer, primary_key=True)
    region_name = Column(String(50), nullable=False)

    country = relationship(
        "´Country", back_populates="region", cascade="all, delete-orphan")

    @validator('region_name')
    def field_country_name_cannot_be_null(cls, region_name):
        if not region_name.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    def __repr__(self):
        return f"Region(id={self.id!r}, " \
               f" regionID={self.regionID!r}," \
               f" region_name={self.region_name!r},"

