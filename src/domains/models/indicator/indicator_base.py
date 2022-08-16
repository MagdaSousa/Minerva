from src.domains import Base,Column,Integer,String


class IndicatorBase(Base):
    __tablename__ = "Indicator"

    id = Column(Integer, primary_key=True)
    indicator_name = Column(String(50),nullable=False)
    indicator_code = Column(String(50),nullable=False)
