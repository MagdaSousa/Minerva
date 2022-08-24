from src.common.Enums import TablesNames
from src.database.database import Base, Column, Integer, String, relationship, ForeignKey
from pydantic import validator



class Region(Base):
    __tablename__ = TablesNames.region.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    region_name = Column(String(50), nullable=False)

    #country_region_fk = relationship("Country", foreign_keys="Country.id")
    country_region_fk = relationship("Country", back_populates="region_country_fk")

    @validator('region_name')
    def field_country_name_cannot_be_null(cls, region_name):
        if not region_name.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    def __repr__(self):
        return f"Region(id={self.id!r}, " \
               f" region_name={self.region_name!r}"
