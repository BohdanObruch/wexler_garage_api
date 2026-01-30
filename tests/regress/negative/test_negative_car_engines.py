import allure
import pytest
from http import HTTPStatus

from garage_api.clients import CarEnginesClient
from tests.data.invalid_params import EDGE_PAGINATION_PARAMS, INVALID_PAGINATION_PARAMS
from tests.helpers.negative_assertions import (
    assert_not_found_or_error,
    assert_not_server_error,
)
from tests.fixtures.types import CarEngineFixture


class TestCarEnginesNegative:
    @allure.tag("regress")
    @pytest.mark.parametrize("params", INVALID_PAGINATION_PARAMS)
    def test_list_car_engines_invalid_pagination(
        self,
        car_engines_client: CarEnginesClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid pagination"):
            response = car_engines_client.list_car_engines_api(params=params)
        with allure.step("Assert no server error for pagination validation"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize("params", EDGE_PAGINATION_PARAMS)
    def test_list_car_engines_edge_pagination(
        self,
        car_engines_client: CarEnginesClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with edge pagination"):
            response = car_engines_client.list_car_engines_api(params=params)
        with allure.step("Assert no server error for edge pagination"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"volume": "big"}, id="volume_string"),
            pytest.param({"production_year": "year"}, id="production_year_string"),
        ],
    )
    def test_list_car_engines_invalid_filters(
        self,
        car_engines_client: CarEnginesClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid filters"):
            response = car_engines_client.list_car_engines_api(params=params)
        with allure.step("Assert no server error for invalid filters"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_required"),
            pytest.param({"engine_number": 123}, id="engine_number_int"),
            pytest.param({"engine_number": "", "volume": 1.6}, id="engine_number_empty"),
            pytest.param(
                {"engine_number": "A" * 256, "volume": 1.6},
                id="engine_number_too_long",
            ),
            pytest.param({"engine_number": "ABC123", "volume": "1.6"}, id="volume_str"),
            pytest.param(
                {"engine_number": "ABC123", "production_year": "year"},
                id="production_year_str",
            ),
            pytest.param(
                {"engine_number": "ABC123", "origin": "A" * 31},
                id="origin_too_long",
            ),
            pytest.param(
                {"engine_number": "ABC123", "production_year": -1},
                id="production_year_negative",
            ),
            pytest.param(
                {"engine_number": "ABC123", "production_year": 4294967296},
                id="production_year_too_large",
            ),
        ],
    )
    def test_create_car_engine_invalid_payload(
        self,
        car_engines_client: CarEnginesClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create car engine with invalid payload"):
            response = car_engines_client._request(
                "POST", "/car_engines/", data=payload
            )
        with allure.step("Assert no server error for invalid create payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_required"),
            pytest.param({"engine_number": 123}, id="engine_number_int"),
            pytest.param(
                {"engine_number": "A" * 256, "volume": 1.6},
                id="engine_number_too_long",
            ),
        ],
    )
    def test_create_car_engine_put_invalid_payload(
        self,
        car_engines_client: CarEnginesClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create car engine (PUT) with invalid payload"):
            response = car_engines_client._request(
                "PUT", "/car_engines/put/", data=payload
            )
        with allure.step("Assert no server error for invalid create PUT payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_get_car_engine_not_found(self, car_engines_client: CarEnginesClient):
        with allure.step("Request non-existent car engine"):
            response = car_engines_client.get_car_engine_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"engine_number": 123}, id="engine_number_int"),
            pytest.param({"volume": "1.6"}, id="volume_str"),
            pytest.param({"engine_number": "A" * 256}, id="engine_number_too_long"),
            pytest.param({"origin": "A" * 31}, id="origin_too_long"),
            pytest.param({"production_year": -1}, id="production_year_negative"),
            pytest.param({"production_year": 4294967296}, id="production_year_too_large"),
        ],
    )
    def test_update_car_engine_invalid_payload(
        self,
        car_engines_client: CarEnginesClient,
        function_car_engine: CarEngineFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send update car engine with invalid payload"):
            response = car_engines_client._request(
                "PUT",
                f"/car_engines/{function_car_engine.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"engine_number": 123}, id="engine_number_int"),
            pytest.param({"production_year": "year"}, id="production_year_str"),
            pytest.param({"engine_number": "A" * 256}, id="engine_number_too_long"),
            pytest.param({"origin": "A" * 31}, id="origin_too_long"),
            pytest.param({"production_year": -1}, id="production_year_negative"),
            pytest.param({"production_year": 4294967296}, id="production_year_too_large"),
        ],
    )
    def test_partial_update_car_engine_invalid_payload(
        self,
        car_engines_client: CarEnginesClient,
        function_car_engine: CarEngineFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send partial update car engine with invalid payload"):
            response = car_engines_client._request(
                "PATCH",
                f"/car_engines/{function_car_engine.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid partial update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_delete_car_engine_not_found(self, car_engines_client: CarEnginesClient):
        with allure.step("Delete non-existent car engine"):
            response = car_engines_client.delete_car_engine_api(999999999)
        with allure.step("Assert not found or validation error"):
            assert response.status_code in {
                HTTPStatus.NOT_FOUND,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNPROCESSABLE_ENTITY,
            }
