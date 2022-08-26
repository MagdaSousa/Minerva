from sqlalchemy.orm import Session
from src.domains.models.country.country import Country
from loguru import logger


class CountryRepository:
    @staticmethod
    def find_all(db: Session) -> list[Country]:
        try:
            return db.query(Country).all()

        except Exception as err:
            raise logger.error(f"[CountryRepository].[find_all]- ERROR- {err} ")

    @staticmethod
    def find_by_region_id(db: Session, id: int) -> Country:
        try:
            results = db.query(Country).filter(Country.region_id == id).all()
            return results
        except Exception as err:
            raise logger.error(f"[CountryRepository].[find_by_region_id]- ERROR- {err} ")

    @staticmethod
    def find_by_country_id(db: Session, id: int) -> Country:
        try:
            results = db.query(Country.country_name).filter(Country.id == id).first()
            return results
        except Exception as err:
            raise logger.error(f"[CountryRepository].[find_by_country_id]- ERROR- {err} ")

    @staticmethod
    def find_by_country_code(db: Session, code: str) -> Country:
        try:
            results = db.query(Country).filter(Country.country_code == code).first()
            return results
        except Exception as err:
            raise logger.error(f"[CountryRepository].[find_by_country_code]- ERROR- {err} ")

    @staticmethod
    def find_by_country_name(db: Session, name: str) -> Country:
        try:
            results = db.query(Country).filter(Country.country_name == name).first()
            return results
        except Exception as err:
            raise logger.error(f"[CountryRepository].[find_by_country_name]- ERROR- {err} ")

