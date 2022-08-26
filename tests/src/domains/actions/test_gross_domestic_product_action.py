from src.domains.actions.gross_domestic_product_action import GDPAction, obj_country, obj_association, obj_indicators
from src.routes.routes import app, get_db

obj_action = GDPAction()


class TestGDPAction:
    def test_should_return_All_data_related_to_an_informed_country(self):
        valid_country_code = 'ABW'
        result = obj_action.find_by_country_code_or_country_name(get_db(), valid_country_code)
        assert len(result) == 3
