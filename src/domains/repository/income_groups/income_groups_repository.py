from sqlalchemy.orm import Session
from src.domains.models.income_groups.invome_groups import IncomeGroups
from loguru import logger


class IncomeGroupsRepository:

    @staticmethod
    def find_by_income_groups_id(db: Session, id: int) -> IncomeGroups:
        try:
            result = db.query(IncomeGroups).filter(IncomeGroups.id == id)
            return result
        except Exception as err:
            raise logger.error(f"[IncomeGroupsRepository].[find_by_income_groups_id]- ERROR- {err} ")

    @staticmethod
    def find_by_income_groups_name(db: Session, name: str) -> IncomeGroups:
        try:
            result = db.query(IncomeGroups).filter(IncomeGroups.region_name == name)
            return result
        except Exception as err:
            raise logger.error(f"[IncomeGroupsRepository].[find_by_income_groups_name]- ERROR- {err} ")
