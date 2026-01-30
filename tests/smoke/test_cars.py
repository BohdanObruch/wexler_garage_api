import allure
import pytest
from garage_api.clients import CarsClient
from garage_api.schemas.responses import CarsListResponseSchema
from tests.data.pagination import PAGINATION_PARAMS
from tests.helpers.list_assertions import assert_list_response


class TestCars:
    @allure.tag("smoke")
    @pytest.mark.parametrize("params", PAGINATION_PARAMS)
    def test_list_cars(self, cars_client: CarsClient, params: dict[str, int] | None):
        response = cars_client.list_cars_api(params=params)
        assert_list_response(response, CarsListResponseSchema, params=params)
