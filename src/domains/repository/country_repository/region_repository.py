from sqlalchemy.orm import Session
from src.domains.models.country.region import Region
from loguru import logger


class RegionRepository:
    @staticmethod
    def find_all(db: Session) -> list[Region]:
        try:
            return db.query(Region).all()

        except Exception as err:
            raise logger.error(f"[RegionRepository].[find_all]- ERROR- {err} ")

    @staticmethod
    def save(db: Session, region: Region) -> Region:
        try:
            if region.regionID:
                db.merge(region)
            else:
                db.add(region)
            db.commit()
            return region

        except Exception as err:
            raise logger.error(f"[RegionRepository].[save]- ERROR- {err} ")

    @staticmethod
    def find_by_id(db: Session, id: int) -> Region:
        try:
            result = db.query(Region).filter(Region.id == id).first()
            return result
        except Exception as err:
            raise logger.error(f"[RegionRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def find_by_region_name(db: Session, name: str) -> Region:
        try:
            result = db.query(Region).filter(Region.region_name == name).first()
            return result
        except Exception as err:
            raise logger.error(f"[RegionRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        try:
            return db.query(Region).filter(Region.id == id).first() is not None

        except Exception as err:
            raise logger.error(f"[RegionRepository].[exists_by_id]- ERROR- {err} ")

    @staticmethod
    def delete(db: Session, id: int) -> None:
        try:
            region = db.query(Region).filter(Region.id == id).first()
            if region is not None:
                db.delete(region)
                db.commit()
        except Exception as err:
            raise logger.error(f"[RegionRepository].[delete]- ERROR- {err} ")
