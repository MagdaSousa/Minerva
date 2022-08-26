from sqlalchemy.orm import Session
from loguru import logger
from src.domains.repository.period.period_repository import PeriodRepository

obj_period = PeriodRepository


class PeriodAction:
    """
    PeriodAction
    """

    @staticmethod
    def find_by_period_range(db: Session, initial_period:int,final_period:int) -> list:
        try:
            periods_list =[]
            period_list_names = obj_period.find_by_period(db, initial_period,final_period)
            for values in period_list_names:
                periods_list.append(values.id)

            return periods_list
        except Exception as err:
            raise logger.error(f"[PeriodAction].[find_by_period_range]- ERROR- {err} ")