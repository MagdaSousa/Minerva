from sqlalchemy.orm import Session
from src.domains.models.country.region import Region
from loguru import logger


class RegionRepository:

    @staticmethod
    def find_by_egion_name(db: Session, name:str) -> Region:
        try:
            results = db.query(Region).filter(Region.region_name == name)

            return results
        except Exception as err:
            raise logger.error(f"[PeriodRepository].[find_by_period]- ERROR- {err} ")

