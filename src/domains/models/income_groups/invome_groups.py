from src.common.Enums import TablesNames
from pydantic import validator
from src.domains import Base, Column, Integer, String, relationship, ForeignKey


class IncomeGroups(Base):
    __tablename__ = TablesNames.income_groups.value

    IncomeGroupID = Column(Integer, primary_key=True)
    ResearchYear = Column(String(50), nullable=False)

    @validator('IncomeGroupID')
    def field_country_name_cannot_be_null(cls, IncomeGroupID):
        if not IncomeGroupID.replace(" ", ""):
            raise ValueError('field country_name cannot be null')

    @validator('IncomeGroupName')
    def field_reference_year_cannot_be_null(cls, income_group_name):
        if not income_group_name.replace(" ", ""):
            raise ValueError('field country_code cannot be null')

    def __repr__(self):
        return f"IncomeGroups(IncomeGroupID={self.IncomeGroupID!r},  IncomeGroupName={self.IncomeGroupName!r})"