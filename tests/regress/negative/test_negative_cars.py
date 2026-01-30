import allure
import pytest
from http import HTTPStatus

from garage_api.clients import CarsClient
from tests.data.invalid_params import EDGE_PAGINATION_PARAMS, INVALID_PAGINATION_PARAMS
from tests.helpers.negative_assertions import (
    assert_not_found_or_error,
    assert_not_server_error,
)
from tests.fixtures.types import CarFixture


class TestCarsNegative:
    @allure.tag("regress")
    @pytest.mark.parametrize("params", INVALID_PAGINATION_PARAMS)
    def test_list_cars_invalid_pagination(
        self,
        cars_client: CarsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid pagination"):
            response = cars_client.list_cars_api(params=params)
        with allure.step("Assert no server error for pagination validation"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize("params", EDGE_PAGINATION_PARAMS)
    def test_list_cars_edge_pagination(
        self,
        cars_client: CarsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with edge pagination"):
            response = cars_client.list_cars_api(params=params)
        with allure.step("Assert no server error for edge pagination"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"car_owner": 123}, id="car_owner_int"),
            pytest.param({"plate_number": 123}, id="plate_number_int"),
            pytest.param({"brand": 123}, id="brand_int"),
            pytest.param({"model": 123}, id="model_int"),
            pytest.param({"engine_number": 123}, id="engine_number_int"),
        ],
    )
    def test_list_cars_invalid_filters(
        self,
        cars_client: CarsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid filters"):
            response = cars_client.list_cars_api(params=params)
        with allure.step("Assert no server error for invalid filters"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_required"),
            pytest.param({"plate_number": 123, "car_owner": 1}, id="plate_number_int"),
            pytest.param(
                {"plate_number": "ABC12345", "car_owner": "owner"},
                id="car_owner_string",
            ),
            pytest.param(
                {"plate_number": "", "car_owner": 1},
                id="plate_number_empty",
            ),
            pytest.param(
                {"plate_number": "A" * 21, "car_owner": 1},
                id="plate_number_too_long",
            ),
            pytest.param(
                {"plate_number": "ABC12345", "car_owner": 1, "brand": "A" * 256},
                id="brand_too_long",
            ),
            pytest.param(
                {"plate_number": "ABC12345", "car_owner": 1, "model": "A" * 256},
                id="model_too_long",
            ),
            pytest.param(
                {"plate_number": "ABC12345", "car_owner": 1, "engine_number": "A" * 256},
                id="engine_number_too_long",
            ),
        ],
    )
    def test_create_car_invalid_payload(
        self,
        cars_client: CarsClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create car with invalid payload"):
            response = cars_client._request("POST", "/cars/", data=payload)
        with allure.step("Assert no server error for invalid create payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_required"),
            pytest.param({"plate_number": 123, "car_owner": 1}, id="plate_number_int"),
            pytest.param(
                {"plate_number": "A" * 21, "car_owner": 1},
                id="plate_number_too_long",
            ),
        ],
    )
    def test_create_car_put_invalid_payload(
        self,
        cars_client: CarsClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create car (PUT) with invalid payload"):
            response = cars_client._request("PUT", "/cars/put/", data=payload)
        with allure.step("Assert no server error for invalid create PUT payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_get_car_not_found(self, cars_client: CarsClient):
        with allure.step("Request non-existent car"):
            response = cars_client.get_car_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"plate_number": 123}, id="plate_number_int"),
            pytest.param({"car_owner": "owner"}, id="car_owner_string"),
            pytest.param({"plate_number": "A" * 21}, id="plate_number_too_long"),
            pytest.param({"brand": "A" * 256}, id="brand_too_long"),
            pytest.param({"model": "A" * 256}, id="model_too_long"),
            pytest.param({"engine_number": "A" * 256}, id="engine_number_too_long"),
        ],
    )
    def test_update_car_invalid_payload(
        self,
        cars_client: CarsClient,
        function_car: CarFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send update car with invalid payload"):
            response = cars_client._request(
                "PUT",
                f"/cars/{function_car.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"plate_number": 123}, id="plate_number_int"),
            pytest.param({"car_owner": "owner"}, id="car_owner_string"),
            pytest.param({"plate_number": "A" * 21}, id="plate_number_too_long"),
            pytest.param({"brand": "A" * 256}, id="brand_too_long"),
            pytest.param({"model": "A" * 256}, id="model_too_long"),
            pytest.param({"engine_number": "A" * 256}, id="engine_number_too_long"),
        ],
    )
    def test_partial_update_car_invalid_payload(
        self,
        cars_client: CarsClient,
        function_car: CarFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send partial update car with invalid payload"):
            response = cars_client._request(
                "PATCH",
                f"/cars/{function_car.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid partial update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_delete_car_not_found(self, cars_client: CarsClient):
        with allure.step("Delete non-existent car"):
            response = cars_client.delete_car_api(999999999)
        with allure.step("Assert not found or validation error"):
            assert response.status_code in {
                HTTPStatus.NOT_FOUND,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNPROCESSABLE_ENTITY,
            }

    @allure.tag("regress")
    def test_create_car_with_missing_owner(self, cars_client: CarsClient):
        payload = {"plate_number": "ABC12345"}
        with allure.step("Send create car with missing owner"):
            response = cars_client._request("POST", "/cars/", data=payload)
        with allure.step("Assert no server error for missing owner"):
            assert_not_server_error(response)
