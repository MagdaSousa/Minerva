from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from src.domains.repository.indicator_repository.gross_domestic_product_repository import GDPRepository, Session
from src.routes.routes import app, get_db
from fastapi.testclient import TestClient
import requests

client = TestClient(app)


class TestGDPRepository:
    insttance = GDPRepository()

    def test_should_return_all_data_related_to_association_table_id(self):
        period_quantity = 62

        valid_association_id = 1
        result = self.insttance.find_by_associations_id(get_db(), valid_association_id)
        assert len(result) == period_quantity
        assert isinstance([x for x in result][0], GrossDomesticProduct)
