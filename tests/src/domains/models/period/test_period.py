from src.domains.models.period.period import Period


class TestPeriod:

    def test_create_period(self):
        new_association = Period(id=444,
                                 research_year=78,
                                 period_gdp_fk=9)
        assert isinstance(new_association, Period)
