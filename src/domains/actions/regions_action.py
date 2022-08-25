from sqlalchemy.orm import Session
from loguru import logger
from src.domains.repository.region.region_repository import RegionRepository

obj_regions = RegionRepository


class RegionAction:
    """
    RegionAction
    """

    @staticmethod
    def find_by_region_name(db: Session, id: int) -> RegionRepository:
        try:

             regions_info = obj_regions.find_by_egion_name(db, id)

             return regions_info
        except Exception as err:
            raise logger.error(f"[RegionAction].[find_by_region_name]- ERROR- {err} ")

