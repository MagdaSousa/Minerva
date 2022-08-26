from sqlalchemy.orm import Session
from src.domains.models.country.region import Region
from loguru import logger


class RegionRepository:

    @staticmethod
    def find_by_region_name(db: Session, name:str) -> Region:
        try:
            results = db.query(Region).filter(Region.region_name == name).first()

            return results
        except Exception as err:
            raise logger.error(f"[RegionRepository].[find_by_region_name]- ERROR- {err} ")

    @staticmethod
    def find_all_regions_names(db: Session) -> [Region]:
        try:
            results = db.query(Region).all()

            return results
        except Exception as err:
            raise logger.error(f"[RegionRepository].[find_all_regions_names]- ERROR- {err} ")

