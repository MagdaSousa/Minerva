from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct


class TestGrossDomesticProduct:

    def test_create_GrossDomesticProduct(self):
        new_association = GrossDomesticProduct(id=76,
                                               value_per_period=45,
                                               association_id=534,
                                               period_id=5767,

                                               gdp_period_fk=676,
                                               association_gdp_fk=43545, )
        assert isinstance(new_association, GrossDomesticProduct)
