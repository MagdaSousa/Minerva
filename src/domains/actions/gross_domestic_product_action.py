from sqlalchemy.orm import Session
from src.domains.actions.association_action import AssociationAction
from src.domains.actions.country_action import CountryAction
from src.domains.actions.indicators_action import IndicatorsAction
from src.domains.repository.indicator_repository.cross_domestic_product_repository import GDPRepository
from src.domains.repository.indicator_repository.indicator_repository import Indicators
from src.domains.repository.country_repository.country_repopsitory import CountryRepository
from src.domains.actions.income_groups_actions import IncomeGroupsAction
from loguru import logger

obj_country = CountryAction
obj_association = AssociationAction
obj_indicators = IndicatorsAction
obj_income_groups = IncomeGroupsAction

class GDPAction:
    """
    GDP -Gross Domestic Product
    """

    @staticmethod
    def find_by_country_code_or_country_name(db: Session, item: str) -> [GDPRepository, CountryRepository, Indicators]:
        try:
            if len(item) == 3:
                country_infos = obj_country.find_by_country_code(db, item)

            else:
                country_infos = obj_country.find_by_country_name(db, item)

            association_infos = obj_association.find_by_country_id(db, country_infos.id)

            indicators_infos = obj_indicators.find_by_indicator_id(db, association_infos.indicators_id)
            income_infos = obj_income_groups.find_by_income_groups_id(db, country_infos.income_group_id)

            gdp = GDPRepository.find_by_associations_id(db, association_infos.id)

            return [gdp, country_infos, indicators_infos, income_infos]

        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_country_code_or_country_name]- ERROR- {err} ")

    @staticmethod
    def find_growth_rate_by_code_or_country_namey(db: Session, item: str) -> GDPRepository:
        try:
            try:
                if len(item) == 3:
                    country_infos = obj_country.find_by_country_code(db, item)

                else:
                    country_infos = obj_country.find_by_country_name(db, item)

                association_infos = obj_association.find_by_country_id(db, country_infos.id)

                gdp = GDPRepository.find_by_associations_id(db, association_infos.id)

                return [gdp, country_infos]

            except Exception as err:
                raise logger.error(f"[GDPAction].[find_by_country_code_or_country_name]- ERROR- {err} ")
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_growth_rate]- ERROR- {err} ")

    @staticmethod
    def find_by_region_name(db: Session, name: str) -> GDPRepository:

        try:

            gdp = GDPRepository.find_gdp_by_region_name(db, name)
            logger.info(f"[GDPAction].[find_by_region_name]- GDP- {gdp} ")
            return gdp
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_region_name]- ERROR- {err} ")

    @staticmethod
    def find_average_gdp_by_country(db: Session, intial_period: int, final_period: int) -> GDPRepository:
        try:

            gdp = GDPRepository.find_gdp_by_region_name(db, intial_period, final_period)

            return gdp
        except Exception as err:
            raise logger.error(f"[GDPAction].[find_by_region_name]- ERROR- {err} ")
