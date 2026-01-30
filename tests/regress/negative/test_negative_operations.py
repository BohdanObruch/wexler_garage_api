import allure
import pytest
from http import HTTPStatus

from garage_api.clients import OperationsClient
from tests.data.invalid_params import EDGE_PAGINATION_PARAMS, INVALID_PAGINATION_PARAMS
from tests.helpers.negative_assertions import (
    assert_client_or_server_error,
    assert_not_found_or_error,
    assert_not_server_error,
)
from tests.fixtures.types import OperationFixture


class TestOperationsNegative:
    @allure.tag("regress")
    @pytest.mark.parametrize("params", INVALID_PAGINATION_PARAMS)
    def test_list_operations_invalid_pagination(
        self,
        operations_client: OperationsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid pagination"):
            response = operations_client.list_operations_api(params=params)
        with allure.step("Assert no server error for pagination validation"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize("params", EDGE_PAGINATION_PARAMS)
    def test_list_operations_edge_pagination(
        self,
        operations_client: OperationsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with edge pagination"):
            response = operations_client.list_operations_api(params=params)
        with allure.step("Assert no server error for edge pagination"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"final_price": "cheap"}, id="final_price_string"),
            pytest.param({"operation_timestamp": 123}, id="timestamp_int"),
            pytest.param({"payment": 123}, id="payment_int"),
            pytest.param({"operation_status": 123}, id="status_int"),
            pytest.param({"car": 123}, id="car_int"),
            pytest.param({"service": 123}, id="service_int"),
        ],
    )
    def test_list_operations_invalid_filters(
        self,
        operations_client: OperationsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid filters"):
            response = operations_client.list_operations_api(params=params)
        with allure.step("Assert no server error for invalid filters"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_required"),
            pytest.param({"car": "car", "service": 1}, id="car_string"),
            pytest.param({"car": 1, "service": "service"}, id="service_string"),
            pytest.param({"car": 1, "service": 2, "final_price": 123}, id="price_int"),
            pytest.param(
                {"car": 1, "service": 2, "final_price": "free"},
                id="price_string_not_decimal",
            ),
            pytest.param(
                {"car": 1, "service": 2, "operation_status": "A" * 31},
                id="status_too_long",
            ),
        ],
    )
    def test_create_operation_invalid_payload(
        self,
        operations_client: OperationsClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create operation with invalid payload"):
            response = operations_client._request("POST", "/operations/", data=payload)
        with allure.step("Assert no server error for invalid create payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_get_operation_not_found(self, operations_client: OperationsClient):
        with allure.step("Request non-existent operation"):
            response = operations_client.get_operation_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"car": "car"}, id="car_string"),
            pytest.param({"service": "service"}, id="service_string"),
            pytest.param({"operation_status": "A" * 31}, id="status_too_long"),
            pytest.param({"final_price": "free"}, id="price_string_not_decimal"),
        ],
    )
    def test_update_operation_invalid_payload(
        self,
        operations_client: OperationsClient,
        function_operation: OperationFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send update operation with invalid payload"):
            response = operations_client._request(
                "PUT",
                f"/operations/{function_operation.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"operation_status": 123}, id="status_int"),
            pytest.param({"final_price": 123}, id="price_int"),
            pytest.param({"operation_status": "A" * 31}, id="status_too_long"),
            pytest.param({"final_price": "free"}, id="price_string_not_decimal"),
        ],
    )
    def test_partial_update_operation_invalid_payload(
        self,
        operations_client: OperationsClient,
        function_operation: OperationFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send partial update operation with invalid payload"):
            response = operations_client._request(
                "PATCH",
                f"/operations/{function_operation.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid partial update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_delete_operation_not_found(self, operations_client: OperationsClient):
        with allure.step("Delete non-existent operation"):
            response = operations_client.delete_operation_api(999999999)
        with allure.step("Assert not found or validation error"):
            assert response.status_code in {
                HTTPStatus.NOT_FOUND,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNPROCESSABLE_ENTITY,
            }

    @allure.tag("regress")
    def test_finish_operation_not_found(self, operations_client: OperationsClient):
        with allure.step("Finish non-existent operation"):
            response = operations_client.finish_operation_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    def test_mark_in_progress_not_found(self, operations_client: OperationsClient):
        with allure.step("Mark in-progress for non-existent operation"):
            response = operations_client.mark_in_progress_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    def test_stop_operation_not_found(self, operations_client: OperationsClient):
        with allure.step("Stop non-existent operation"):
            response = operations_client.stop_operation_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"plate_number": ""}, id="plate_number_empty"),
            pytest.param({"service_name": ""}, id="service_name_empty"),
            pytest.param({"plate_number": 123, "service_name": "S"}, id="plate_number_int"),
            pytest.param({"plate_number": "AAA11111"}, id="missing_service_name"),
            pytest.param({"service_name": "S"}, id="missing_plate_number"),
            pytest.param({"final_price": "cheap"}, id="final_price_string"),
            pytest.param({"operation_status": 123}, id="status_int"),
            pytest.param({"payment": 123}, id="payment_int"),
        ],
    )
    def test_init_operation_invalid_params(
        self,
        operations_client: OperationsClient,
        params: dict[str, object],
    ):
        with allure.step("Send init operation with invalid params"):
            response = operations_client._request(
                "GET", "/operations/init/", params=params
            )
        with allure.step("Assert no server error for invalid init params"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"discount": "ten"}, id="discount_string"),
            pytest.param({"discount": -1}, id="discount_negative"),
        ],
    )
    def test_apply_discount_invalid_params(
        self,
        operations_client: OperationsClient,
        function_operation: OperationFixture,
        params: dict[str, object],
    ):
        with allure.step("Send apply_discount with invalid params"):
            response = operations_client._request(
                "GET",
                f"/operations/{function_operation.response.id}/apply_discount/",
                params=params,
            )
        with allure.step("Assert client or server error for invalid discount"):
            assert_client_or_server_error(response)
