from src.common.Enums import TablesNames
from pydantic import validator

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from src.database.database import Base


class IncomeGroups(Base):
    __tablename__ = TablesNames.income_groups.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    income_level = Column(String(60), nullable=False)

    country_income_fk = relationship("Country", back_populates="income_country_fk")

    @validator('income_level')
    def field_country_name_cannot_be_null(cls, income_level):
        if not income_level.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    def __repr__(self):
        return f"IncomeGroups(id={self.id!r},  income_level={self.income_level!r})"
