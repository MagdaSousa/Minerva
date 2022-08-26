from sqlalchemy.orm import Session
from loguru import logger
from src.domains.repository.indicator_repository.indicator_repository import IndicatorsRepository

obj_indicators = IndicatorsRepository
class IndicatorsAction:
    """
    IndicatorsAction
    """

    @staticmethod
    def find_by_indicator_id(db: Session, id: int) -> IndicatorsRepository:
        try:

            indicator_info = obj_indicators.find_by_indicators_id(db, id)

            return indicator_info
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_indicator_id]- ERROR- {err} ")

    @staticmethod
    def find_by_indicator_code(db: Session, code: str) -> IndicatorsRepository:
        try:

            indicator_info = obj_indicators.find_by_indicators_code(db, code)

            return indicator_info
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_indicator_code]- ERROR- {err} ")