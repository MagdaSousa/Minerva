from sqlalchemy.orm import Session
from loguru import logger
from src.domains.repository.region.region_repository import RegionRepository

obj_regions = RegionRepository


class RegionAction:
    """
    RegionAction
    """

    @staticmethod
    def find_by_region_name(db: Session, name: str) -> RegionRepository:
        try:

            regions_info = obj_regions.find_by_region_name(db, name)

            return regions_info
        except Exception as err:
            raise logger.error(f"[RegionAction].[find_by_region_name]- ERROR- {err} ")

    @staticmethod
    def find_regions(db: Session) ->[RegionRepository] :
        try:

            regions_info = obj_regions.find_all_regions_names(db)

            return regions_info
        except Exception as err:
            raise logger.error(f"[RegionAction].[find_by_region_name]- ERROR- {err} ")
