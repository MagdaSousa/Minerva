from src.routes.routes import app, get_db
from fastapi.testclient import TestClient
import requests

client = TestClient(app)


class TestApi:
    def my_second_override(self):
        return {"another": "override"}

    def test_get_country_by_code(self, fastapi_dep, response_api):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            country_code = 'UKR'
            response = client.get(f"/gdp/country/{country_code}")
            assert response.status_code == 200
            assert response.json() == response_api

    def test_get_country_by_name(self, fastapi_dep, response_api):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            country_name = 'Ukraine'
            response = client.get(f"/gdp/country/{country_name}")
            assert response.status_code == 200
            assert response.json() == response_api

    def test_get_country_by_name_error(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_value = 1
            response = client.get(f"/gdp/country/{invalid_value}")
            assert response.status_code == 400
            assert response.json() == {'detail': '1 is not a string'}

    def test_get_country_by_code_error(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_value = 1
            response = client.get(f"/gdp/country/{invalid_value}")
            assert response.status_code == 400
            assert response.json() == {'detail': '1 is not a string'}

    def test_get_rate_by_country(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: "plain_override_object"
                }
        ):
            response = client.get(f"/gdp/rate/country/{item}")
            assert response.status_code == 400
            assert response.json() == {
                "first_dep": "plain_override_object",
                "second_dep": {"another": "override"},
            }

    def test_get_rate_by_country_error(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: "plain_override_object"
                }
        ):
            response = client.get(f"/gdp/rate/country/{item}")
            assert response.status_code == 404
            assert response.json() == {
                "first_dep": "plain_override_object",
                "second_dep": {"another": "override"},
            }

    def test_get_region(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: "plain_override_object"
                }
        ):
            response = client.get(f"/gdp/region/{item}")
            assert response.status_code == 404
            assert response.json() == {
                "first_dep": "plain_override_object",
                "second_dep": {"another": "override"},
            }

    def test_get_region_error(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: "plain_override_object"
                }
        ):
            response = client.get(f"/gdp/region/{item}")
            assert response.status_code == 404
            assert response.json() == {
                "first_dep": "plain_override_object",
                "second_dep": {"another": "override"},
            }
