from sqlalchemy.orm import Session
from src.domains.repository.country_repository.country_repopsitory import CountryRepository
from loguru import logger


class CountryAction:
    """
    CountryAction
    """

    @staticmethod
    def find_by_country_code(db: Session, code: str) -> CountryRepository:
        try:

            return CountryRepository.find_by_country_code(db, code)
        except Exception as err:
            raise logger.error(f"[CountryAction].[find_by_country_code_or_country_name]- ERROR- {err} ")

    @staticmethod
    def find_by_country_name(db: Session, name: str) -> CountryRepository:
        try:
            return CountryRepository.find_by_country_name(db, name)
        except Exception as err:
            raise logger.error(f"[CountryAction].[find_by_country_code_or_country_name]- ERROR- {err} ")

    @staticmethod
    def find_by_region_id(db: Session, id: int) -> [CountryRepository]:
        try:

            return CountryRepository.find_by_region_id(db, id)
        except Exception as err:
            raise logger.error(f"[CountryAction].[find_by_region_id]- ERROR- {err} ")

    @staticmethod
    def find_by_country_id(db: Session, id: int) -> [CountryRepository]:
        try:

            return CountryRepository.find_by_country_id(db, id)
        except Exception as err:
            raise logger.error(f"[CountryAction].[find_by_country_id]- ERROR- {err} ")