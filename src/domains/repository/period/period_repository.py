from sqlalchemy.orm import Session
from src.domains.models.period.period import Period
from loguru import logger


class PeriodRepository:

    @staticmethod
    def find_by_period(db: Session, intial_period: int, final_period: int) -> [Period]:
        try:
            results = db.query(Period).filter(Period.research_year >= intial_period,Period.research_year <= final_period).all()

            return results
        except Exception as err:
            raise logger.error(f"[PeriodRepository].[find_by_period]- ERROR- {err} ")

