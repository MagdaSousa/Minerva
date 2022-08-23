from sqlalchemy.orm import Session
from src.domains.models.indicators import Indicator
from loguru import logger


class IndicatorRepository:
    @staticmethod
    def find_all(db: Session) -> list[Indicator]:
        try:
            return db.query(Indicator).all()

        except Exception as err:
            raise logger.error(f"[IndicatorRepository].[find_all]- ERROR- {err} ")

    @staticmethod
    def save(db: Session, indicator: Indicator) -> Indicator:
        try:
            if Indicator.id:
                db.merge(indicator)
            else:
                db.add(indicator)
            db.commit()
            return indicator

        except Exception as err:
            raise logger.error(f"[IndicatorRepository].[save]- ERROR- {err} ")

    @staticmethod
    def find_by_id(db: Session, id: int) -> Indicator:
        try:
            return db.query(Indicator).filter(Indicator.IndicatorID == id).first()
        except Exception as err:
            raise logger.error(f"[IndicatorRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def find_by_Indicator_code(db: Session, id: int) -> Indicator:
        try:
            return db.query(Indicator).filter(Indicator.IndicatorID == id).first()
        except Exception as err:
            raise logger.error(f"[IndicatorRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        try:
            return db.query(Indicator).filter(Indicator.IndicatorID == id).first() is not None

        except Exception as err:
            raise logger.error(f"[IndicatorRepository].[exists_by_id]- ERROR- {err} ")

    @staticmethod
    def delete(db: Session, id: int) -> None:
        try:
            indicator = db.query(Indicator).filter(Indicator.IndicatorID == id).first()
            if indicator is not None:
                db.delete(indicator)
                db.commit()
        except Exception as err:
            raise logger.error(f"[IndicatorRepository].[delete_by_id]- ERROR- {err} ")
