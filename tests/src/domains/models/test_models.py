from src.domains.models.association_tables.association_tables import Association
from src.domains.models.country.country import Country
from src.domains.models.country.region import Region
from src.domains.models.income_groups.invome_groups import IncomeGroups
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from src.domains.models.indicators.indicators import Indicators
from src.domains.models.period.period import Peri
import pytest

from faker import Faker

fake = Faker()

fake.ci()
# 'Lucy Cechtelar'

fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

fake.text()


class TestCreateModels:

    def test_create_models(self):
        country_dict = {"id": 122,
                        "country_name": row['Country Name'],
                        "country_code": row['Country Code'],
                        "region_id": row['RegionId'],
                        "income_group_id": row['IncomeGroupsId']
                        }
        obj_country = Country(*country_dict)

        assert obj_country.country_code == country_dict['id']
        assert obj_country.country_name == 122

    def test_should_return_an_exception_when_an_empty_field_is_sent(self):
        country_dict = {"id": 122,
                        "country_name": row['Country Name'],
                        "country_code": row['Country Code'],
                        "region_id": row['RegionId'],
                        "income_group_id": row['IncomeGroupsId']
                        }
        obj_country = Country(*country_dict)

        assert obj_country.country_code == country_dict['id']
        assert obj_country.country_name == 122
