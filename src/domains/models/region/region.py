from src.domains import Base, Column, Integer, String, relationship, ForeignKey


class Region(Base):
    __tablename__ = "Region"

    id = Column(Integer, primary_key=True)
    country_Name = Column(String(50), nullable=False)
    country_code = Column(String(50), nullable=False)
    region = Column(String(50), nullable=False)
    region_and_indicator = relationship(
        "´region_and_indicator", back_populates="region", cascade="all, delete-orphan")

    def __repr__(self):
        return f"GrossDomesticProduct(id={self.id!r}, " \
               f"country_Name={self.country_Name!r}," \
               f" country_code={self.country_code!r}," \
               f" region={self.region!r}," \
               f" region_and_indicator={self.region_and_indicator!r})"
