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
    def find_by_associations_id_and_period(db: Session, period_list: list) -> GrossDomesticProduct:
        try:
            # results = db.query(GrossDomesticProduct.association_id,sum(GrossDomesticProduct.value_per_period)).filter(GrossDomesticProduct.period_id.in_(period_list)).groupby(GrossDomesticProduct.association_id)

            from sqlalchemy.sql import func
            results = db.query(GrossDomesticProduct.association_id, func.avg(GrossDomesticProduct.value_per_period)
                               .label('average')).filter(GrossDomesticProduct.period_id.in_(period_list)) \
                .group_by(GrossDomesticProduct.association_id).all()

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
    def find_by_period_id(db: Session, period_list: list) -> GrossDomesticProduct:
        try:

            results = db.query(GrossDomesticProduct.association_id, sum(GrossDomesticProduct.value_per_period)).filter(
                GrossDomesticProduct.period_id.in_(period_list)).Groupby(GrossDomesticProduct.association_id).all()

            return results
        except Exception as err:
            raise logger.error(f"[GrossDomesticProductRepository].[find_by_period_id]- ERROR- {err} ")
