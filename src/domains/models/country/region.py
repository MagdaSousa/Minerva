from src.common.Enums import TablesNames
from src.domains import Base, Column, Integer, String, relationship


class Region(Base):
    __tablename__ = TablesNames.region.value

    regionID = Column(Integer, primary_key=True)
    region_name = Column(String(50), nullable=False)

    country = relationship(
        "´Country", back_populates="region", cascade="all, delete-orphan")

    def __repr__(self):
        return f"GrossDomesticProduct(id={self.id!r}, " \
               f" regionID={self.regionID!r}," \
               f" region_name={self.region_name!r},"
