from sqlalchemy.orm import Session
from loguru import logger
from src.domains.repository.income_groups.income_groups_repository import IncomeGroupsRepository

obj_income_groups = IncomeGroupsRepository


class IncomeGroupsAction:
    """
    IncomeGroupsAction
    """

    @staticmethod
    def find_by_income_groups_id(db: Session, id: int) -> IncomeGroupsRepository:
        try:

            income_groups_info = obj_income_groups.find_by_income_groups_id(db, id)

            return income_groups_info
        except Exception as err:
            raise logger.error(f"[IncomeGroupsAction].[find_by_indicator_id]- ERROR- {err} ")

    @staticmethod
    def find_by_income_groups_code(db: Session, code: str) -> IncomeGroupsRepository:
        try:

            income_groups_info = obj_income_groups.find_by_income_groups_code(db, code)

            return income_groups_info
        except Exception as err:
            raise logger.error(f"[IncomeGroupsAction].[find_by_income_groups_code]- ERROR- {err} ")
