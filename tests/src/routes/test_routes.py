from src.routes.routes import app, get_db
from fastapi.testclient import TestClient
import requests

client = TestClient(app)


class TestApi:

    def test_gshould_return_a_json_with_the_data_of_the_queried_city_code(self, fastapi_dep, response_api):
        with fastapi_dep(app).override(
                {
                    get_db: get_db()
                }
        ):
            country_code = 'UKR'
            response = client.get(f"/gdp/country/{country_code}")
            assert response.status_code == 200
            assert response.json() == response_api

    def test_gshould_return_a_json_with_the_data_of_the_queried_city(self, fastapi_dep, response_api):
        with fastapi_dep(app).override(
                {
                    get_db: get_db()
                }
        ):
            country_name = 'Ukraine'
            response = client.get(f"/gdp/country/{country_name}")
            assert response.status_code == 200
            assert response.json() == response_api

    def test_should_return_an_exception_on_receiving_an_unexpected_type(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_value = 1
            response = client.get(f"/gdp/country/{invalid_value}")
            assert response.status_code == 400
            assert response.json() == {'detail': '1 is not a string'}

    def test_should_return_an_exception_when_receiving_an_unregistered_country(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_value = 'invalid country'
            response = client.get(f"/gdp/country/{invalid_value}")
            assert response.status_code == 400
            assert response.json() == {'detail': 'invalid country is not a string'}

    def test_should_return_an_exception_when_receiving_an_unregistered_code(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_value = 'JJJ'
            response = client.get(f"/gdp/country/{invalid_value}")
            assert response.status_code == 400
            assert response.json() == {'detail': 'invalid country is not a string'}

    # Gross Rate

    def test_gshould_return_a_json_with_gross_rate_of_the_queried_city_code(self, fastapi_dep, response_api):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            country_code = 'UKR'
            response = client.get(f"gdp/rate/country/{country_code}")
            assert response.status_code == 200
            assert response.json() == response_api

    def test_gshould_return_a_json_with_the_gross_rate_of_the_queried_city(self, fastapi_dep, response_api):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            country_name = 'Ukraine'
            response = client.get(f"gdp/rate/country/{country_name}")
            assert response.status_code == 200
            assert response.json() == response_api

    def test_should_return_an_exception_on_receiving_an_unexpected_type_by_gross_rate(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_value = 1
            response = client.get(f"gdp/rate/country/{invalid_value}")
            assert response.status_code == 400
            assert response.json() == {'detail': '1 is not a string'}

    def test_should_return_an_exception_when_receiving_an_unregistered_country_by_gross_rate(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_value = 'invalid country'
            response = client.get(f"gdp/rate/country/{invalid_value}")
            assert response.status_code == 400
            assert response.json() == {'detail': 'invalid country is not a string'}

    def test_should_return_an_exception_when_receiving_an_unregistered_code_by_gross_rate(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_value = 'JJJ'
            response = client.get(f"gdp/rate/country/{invalid_value}")
            assert response.status_code == 400
            assert response.json() == {'detail': 'invalid country is not a string'}

    # By region

    def test_gshould_return_region(self, fastapi_dep, response_api):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            region_name = 'Latin America & Caribbean'
            response = client.get(f"gdp/region/{region_name}")
            assert response.status_code == 200

    def test_should_return_an_exception_on_receiving_an_unexpected_type_region(self, fastapi_dep):
        with fastapi_dep(app).override(
                {
                    get_db: get_db
                }
        ):
            invalid_region_name = 1
            response = client.get(f"gdp/region/{invalid_region_name}")
            assert response.status_code == 400
            assert response.json() == {'detail': '1 is not a string'}
