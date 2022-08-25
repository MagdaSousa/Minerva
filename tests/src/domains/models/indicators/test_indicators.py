from src.domains.models.indicators.indicators import Indicators


class TestIndicators:

    def test_create_indicators(self):
        new_association = Indicators(id=990,
                                     indicator_name='indicator test',
                                     indicator_code='234DEG',
                                     country_indicators_fk=8)
        assert isinstance(new_association, Indicators)
