from src.domains.repository.association_repository.association_repository import AssociationRepository
from sqlalchemy.orm import Session
from loguru import logger


class AssociationAction:
    """
    AssociationAction
    """

    @staticmethod
    def find_by_country_id(db: Session, id: int) -> AssociationRepository:
        try:

            association_infos = AssociationRepository.find_by_country_id(db, id)

            return association_infos
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_country_code_or_country_name]- ERROR- {err} ")

    @staticmethod
    def find_by_indicator_id(db: Session, id: int) -> AssociationRepository:
        try:

            indicators_id = AssociationRepository.find_by_indicators_id(db, id)

            return indicators_id
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_country_code_or_country_name]- ERROR- {err} ")

    @staticmethod
    def find_by_country_ids(db: Session, id: int) -> AssociationRepository:
        try:

            indicators_id = AssociationRepository.find_by_indicators_id(db, id)

            return indicators_id
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_country_code_or_country_name]- ERROR- {err} ")

    @staticmethod
    def find_by_association_id(db: Session, id: int) -> AssociationRepository:
        try:

            indicators_id = AssociationRepository.find_by_association_id(db, id)

            return indicators_id
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_country_code_or_country_name]- ERROR- {err} ")

    @staticmethod
    def find_all_associations(db: Session) -> [list]:
        try:

            associations=  AssociationRepository.find_all(db)




            return associations
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_country_code_or_country_name]- ERROR- {err} ")