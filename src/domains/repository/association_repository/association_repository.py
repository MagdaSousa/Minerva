from sqlalchemy.orm import Session
from src.domains.models.association_tables.association_tables import Association
from loguru import logger


class AssociationRepository:

    @staticmethod
    def find_by_country_id(db: Session, id: int) -> Association:
        try:
            associations_code = db.query(Association).filter(Association.country_id == id).first()
            return associations_code
        except Exception as err:
            raise logger.error(f"[AssociationRepository].[find_by_country_id]- ERROR- {err} ")

    @staticmethod
    def find_by_indicators_id(db: Session, id: int) -> Association.id:
        try:
            associations_code =db.query(Association).filter(Association.indicators_id == id).first()
            return associations_code
        except Exception as err:
            raise logger.error(f"[AssociationRepository].[find_by_indicators_id]- ERROR- {err} ")

    @staticmethod
    def find_by_association_id(db: Session, id: int) -> Association.id:
        try:
            country_id = db.query(Association.country_id).filter(Association.id == id).first()
            return country_id
        except Exception as err:
            raise logger.error(f"[AssociationRepository].[find_by_indicators_id]- ERROR- {err} ")

    @staticmethod
    def find_all(db: Session) -> list:
        try:
            associations = db.query(Association).all()
            return associations
        except Exception as err:
            raise logger.error(f"[AssociationRepository].[find_by_indicators_id]- ERROR- {err} ")
