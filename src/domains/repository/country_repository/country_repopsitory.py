from sqlalchemy.orm import Session
from src.domains.models.country import Country
from loguru import logger


class CountryRepository:
    @staticmethod
    def find_all(db: Session) -> list[Country]:
        try:
            return db.query(Country).all()

        except Exception as err:
            raise logger.error(f"[CountryRepository].[find_all]- ERROR- {err} ")

    @staticmethod
    def save(db: Session, country: Country) -> Country:
        try:
            if country.id:
                db.merge(country)
            else:
                db.add(country)
            db.commit()
            return country

        except Exception as err:
            raise logger.error(f"[CountryRepository].[save]- ERROR- {err} ")

    @staticmethod
    def find_by_id(db: Session, id: int) -> Country:
        try:
            return db.query(Country).filter(Country.countryID == id).first()
        except Exception as err:
            raise logger.error(f"[CountryRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def find_by_country_code(db: Session, id: int) -> Country:
        try:
            return db.query(Country).filter(Country.countryID == id).first()
        except Exception as err:
            raise logger.error(f"[CountryRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        try:
            return db.query(Country).filter(Country.countryID == id).first() is not None

        except Exception as err:
            raise logger.error(f"[CountryRepository].[exists_by_id]- ERROR- {err} ")

    @staticmethod
    def delete(db: Session, id: int) -> None:
        try:
            country = db.query(Country).filter(Country.countryID == id).first()
            if country is not None:
                db.delete(country)
                db.commit()
        except Exception as err:
            raise logger.error(f"[CountryRepository].[delete_by_id]- ERROR- {err} ")
