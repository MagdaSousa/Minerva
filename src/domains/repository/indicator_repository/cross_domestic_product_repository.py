from sqlalchemy.orm import Session
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from loguru import logger


class GDPRepository:
    """
    GDP -Gross Domestic Product
    """


    @staticmethod
    def find_by_associations_id_new(db: Session, association: int) -> GrossDomesticProduct:
        try:
            results = db.query(GrossDomesticProduct).filter(
                GrossDomesticProduct.association_id == association).all()

            return results
        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_by_associations_id]- ERROR- {err} ")


    @staticmethod
    def find_by_associations_id(db: Session, association: int) -> GrossDomesticProduct:
        try:
            results = db.query(GrossDomesticProduct).filter(
                GrossDomesticProduct.association_id == association).all()

            return results
        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_by_associations_id]- ERROR- {err} ")

    @staticmethod
    def find_by_country_code(db: Session, code: int) -> GrossDomesticProduct:
        try:
            return db.query(GrossDomesticProduct).filter(GrossDomesticProduct.association_id == code).all()
        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def find_gdp_by_region_name(db: Session, id: int) -> GrossDomesticProduct:
        try:

            return db.query(GrossDomesticProduct).filter(GrossDomesticProduct.association_id == id).all()
        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def find_all(db: Session) -> list:
        try:
            return db.query(GrossDomesticProduct).all()

        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_all]- ERROR- {err} ")



    @staticmethod
    def exists_by_code(db: Session, id: int) -> bool:
        try:
            return db.query(GrossDomesticProduct).filter(GrossDomesticProduct.GrossDomesticProductID == id).first() is not None

        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[exists_by_id]- ERROR- {err} ")


