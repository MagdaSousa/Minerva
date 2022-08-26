from src.domains.models.country.region import Region


class TestRegion:

    def test_create_country(self):
        new_association = Region(id=1,
                                 region_name=1,
                                 country_region_fk=1)
        assert isinstance(new_association, Region)
