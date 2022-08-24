from sqlalchemy.orm import Session
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from loguru import logger


class GDPRepository:
    """
    GDP -Gross Domestic Product
    """

    @staticmethod
    def find_by_country_code(db: Session, code: int) -> GrossDomesticProduct:
        try:
            return db.query(GrossDomesticProduct).filter(GrossDomesticProduct.association_id == id).first()
        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def find_gdp_by_region_name(db: Session, id: int) -> GrossDomesticProduct:
        try:

            return db.query(GrossDomesticProduct).filter(GrossDomesticProduct.association_id == id).first()
        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_by_id]- ERROR- {err} ")

    @staticmethod
    def find_all(db: Session) -> list:
        try:
            return db.query(GrossDomesticProduct).all()

        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_all]- ERROR- {err} ")

    @staticmethod
    def save(db: Session, gross_domestic_product: GrossDomesticProduct) -> GrossDomesticProduct:
        try:
            if gross_domestic_product.id:
                db.merge(gross_domestic_product)
            else:
                db.add(gross_domestic_product)
            db.commit()
            return gross_domestic_product

        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[save]- ERROR- {err} ")


    @staticmethod
    def exists_by_code(db: Session, id: int) -> bool:
        try:
            return db.query(GrossDomesticProduct).filter(GrossDomesticProduct.GrossDomesticProductID == id).first() is not None

        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[exists_by_id]- ERROR- {err} ")

    @staticmethod
    def delete(db: Session, id: int) -> None:
        try:
            gross_domestic_product = db.query(GrossDomesticProduct).filter(GrossDomesticProduct.GrossDomesticProductID == id).first()
            if gross_domestic_product is not None:
                db.delete(gross_domestic_product)
                db.commit()
        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[delete]- ERROR- {err} ")
