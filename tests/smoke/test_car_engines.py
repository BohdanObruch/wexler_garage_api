import allure
import pytest
from garage_api.clients import CarEnginesClient
from garage_api.schemas.responses import CarEnginesListResponseSchema
from tests.data.pagination import PAGINATION_PARAMS
from tests.helpers.list_assertions import assert_list_response


class TestCarEngines:
    @allure.tag("smoke")
    @pytest.mark.parametrize("params", PAGINATION_PARAMS)
    def test_list_car_engines(
        self,
        car_engines_client: CarEnginesClient,
        params: dict[str, int] | None,
    ):
        response = car_engines_client.list_car_engines_api(params=params)
        assert_list_response(response, CarEnginesListResponseSchema, params=params)
