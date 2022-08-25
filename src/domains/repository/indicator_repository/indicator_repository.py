from sqlalchemy.orm import Session
from src.domains.models.indicators.indicators import Indicators
from loguru import logger


class IndicatorsRepository:
    @staticmethod
    def find_all(db: Session) -> list[Indicators]:
        try:
            return db.query(Indicators).all()

        except Exception as err:
            raise logger.error(f"[IndicatorsRepository].[find_all]- ERROR- {err} ")

    @staticmethod
    def save(db: Session, indicators: Indicators) -> Indicators:
        try:
            if indicators.id:
                db.merge(indicators)
            else:
                db.add(indicators)
            db.commit()
            return indicators

        except Exception as err:
            raise logger.error(f"[IndicatorsRepository].[save]- ERROR- {err} ")

    @staticmethod
    def find_by_indicators_id(db: Session, id: int) -> Indicators:
        try:
            result =db.query(Indicators).filter(Indicators.id == id).all()
            return  result
        except Exception as err:
            raise logger.error(f"[IndicatorsRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def find_by_indicators_code(db: Session, code: str) -> Indicators:
        try:
            result =db.query(Indicators).filter(Indicators.indicator_code == code).all()
            return  result
        except Exception as err:
            raise logger.error(f"[IndicatorsRepository].[find_by_indicators_code]- ERROR- {err} ")

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        try:
            return db.query(Indicators).filter(Indicators.id == id).first() is not None

        except Exception as err:
            raise logger.error(f"[IndicatorsRepository].[exists_by_id]- ERROR- {err} ")

    @staticmethod
    def delete(db: Session, id: int) -> None:
        try:
            results = db.query(Indicators).filter(Indicators.id == id).first()
            if Indicators is not None:
                db.delete(results)
                db.commit()
        except Exception as err:
            raise logger.error(f"[IndicatorsRepository].[delete_by_id]- ERROR- {err} ")
