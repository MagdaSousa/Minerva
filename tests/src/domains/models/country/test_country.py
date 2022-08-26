from src.domains.models.country.country import Country


class TestAssociation:

    def test_create_country(self):
        new_association = Country(id=1,
                                  country_name='teste  country name',
                                  country_code='DFG',
                                  region_id=1,
                                  income_group_id=2,
                                  region_country_fk=4,
                                  income_country_fk=5,
                                  indicator_country_fk=1)
        assert isinstance(new_association, Country)
