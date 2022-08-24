from sqlalchemy.orm import Session

from src.domains.repository.indicator_repository.cross_domestic_product_repository import GDPRepository
from loguru import logger


class GDPAction:
    """
    GDP -Gross Domestic Product
    """

    @staticmethod
    def find_by_country_code_or_country_name(db: Session, item: str) -> GDPRepository:
        try:
            if len(item) == 3:
                gdp = GDPRepository.find_by_country_code(db, item)
            else:
                gdp = GDPRepository.find_by_country_name(db, item)
            return gdp
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_country_code_or_country_name]- ERROR- {err} ")

    @staticmethod
    def find_growth_rate(db: Session, item: str) -> GDPRepository:
        try:
            print(1)
            # if len(item) == 3:
            #     gdp = GDPRepository.find_by_country_code(db, item)
            # else:
            #     gdp = GDPRepository.find_by_country_name(db, item)


        except Exception as err:
            raise logger.error(f"[GDPAction].[find_growth_rate]- ERROR- {err} ")

    @staticmethod
    def find_by_region_name(db: Session, name: str) -> GDPRepository:

        try:
            print(1)
            #
            # gdp = GDPRepository.find_gdp_by_region_name(db, name)
            # logger.info(f"[GDPAction].[find_by_region_name]- GDP- {gdp} ")
            # return gdp
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_region_name]- ERROR- {err} ")

    @staticmethod
    def find_average_gdp_by_country(db: Session, intial_period: int, final_period: int) -> GDPRepository:
        try:
            #print(1)
            #gdp = GDPRepository.find_gdp_by_region_name(db, intial_period, final_period)

            return gdp
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_region_name]- ERROR- {err} ")
