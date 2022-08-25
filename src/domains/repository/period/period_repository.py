from sqlalchemy.orm import Session
from src.domains.models.period.period import Period
from loguru import logger


class PeriodRepository:

    @staticmethod
    def find_by_period(db: Session, intial_period: int, final_period: int) -> Period:
        try:
            results = db.query(Period).filter(
                Period.research_year == intial_period and Period.research_year == final_period).first()

            return results
        except Exception as err:
            raise logger.error(f"[PeriodRepository].[find_by_period]- ERROR- {err} ")

    @staticmethod
    def exists_by_period(db: Session, intial_period: int, final_period: int) -> bool:
        try:
            return db.query(Period).filter(
                Period.research_year == intial_period and Period.research_year == final_period).first() is not None

        except Exception as err:
            raise logger.error(f"[PeriodRepository].[exists_by_period]- ERROR- {err} ")