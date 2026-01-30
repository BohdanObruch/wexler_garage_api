import allure
import pytest
from http import HTTPStatus

from garage_api.clients import CustomersClient
from tests.data.invalid_params import EDGE_PAGINATION_PARAMS, INVALID_PAGINATION_PARAMS
from tests.helpers.negative_assertions import (
    assert_client_or_server_error,
    assert_not_found_or_error,
    assert_not_server_error,
)
from tests.fixtures.types import CustomerFixture


class TestCustomersNegative:
    @allure.tag("regress")
    @pytest.mark.parametrize("params", INVALID_PAGINATION_PARAMS)
    def test_list_customers_invalid_pagination(
        self,
        customers_client: CustomersClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid pagination"):
            response = customers_client.list_customers_api(params=params)
        with allure.step("Assert no server error for pagination validation"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize("params", EDGE_PAGINATION_PARAMS)
    def test_list_customers_edge_pagination(
        self,
        customers_client: CustomersClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with edge pagination"):
            response = customers_client.list_customers_api(params=params)
        with allure.step("Assert no server error for edge pagination"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"passport_number": "abc"}, id="passport_number_string"),
            pytest.param({"age": "old"}, id="age_string"),
            pytest.param({"first_name": 123}, id="first_name_int"),
            pytest.param({"last_name": 123}, id="last_name_int"),
            pytest.param({"email": 123}, id="email_int"),
            pytest.param({"city": 123}, id="city_int"),
        ],
    )
    def test_list_customers_invalid_filters(
        self,
        customers_client: CustomersClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid filters"):
            response = customers_client.list_customers_api(params=params)
        with allure.step("Assert no server error for invalid filters"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_required"),
            pytest.param({"passport_number": "abc"}, id="passport_number_string"),
            pytest.param({"passport_number": 12345678, "age": "old"}, id="age_string"),
            pytest.param({"passport_number": 9223372036854775808}, id="passport_too_large"),
            pytest.param({"age": -1}, id="age_negative"),
            pytest.param({"age": 4294967296}, id="age_too_large"),
            pytest.param({"first_name": "A" * 21}, id="first_name_too_long"),
            pytest.param({"last_name": "A" * 256}, id="last_name_too_long"),
            pytest.param({"email": "A" * 256}, id="email_too_long"),
            pytest.param({"city": "A" * 256}, id="city_too_long"),
        ],
    )
    def test_create_customer_invalid_payload(
        self,
        customers_client: CustomersClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create customer with invalid payload"):
            response = customers_client._request("POST", "/customers/", data=payload)
        with allure.step("Assert no server error for invalid create payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_required"),
            pytest.param({"passport_number": "abc"}, id="passport_number_string"),
            pytest.param({"passport_number": 9223372036854775808}, id="passport_too_large"),
        ],
    )
    def test_create_customer_put_invalid_payload(
        self,
        customers_client: CustomersClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create customer (PUT) with invalid payload"):
            response = customers_client._request("PUT", "/customers/put/", data=payload)
        with allure.step("Assert client or server error for invalid create PUT payload"):
            assert_client_or_server_error(response)

    @allure.tag("regress")
    def test_get_customer_not_found(self, customers_client: CustomersClient):
        with allure.step("Request non-existent customer"):
            response = customers_client.get_customer_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"passport_number": "abc"}, id="passport_number_string"),
            pytest.param({"age": "old"}, id="age_string"),
            pytest.param({"passport_number": 9223372036854775808}, id="passport_too_large"),
            pytest.param({"age": -1}, id="age_negative"),
            pytest.param({"age": 4294967296}, id="age_too_large"),
            pytest.param({"first_name": "A" * 21}, id="first_name_too_long"),
            pytest.param({"last_name": "A" * 256}, id="last_name_too_long"),
            pytest.param({"email": "A" * 256}, id="email_too_long"),
            pytest.param({"city": "A" * 256}, id="city_too_long"),
        ],
    )
    def test_update_customer_invalid_payload(
        self,
        customers_client: CustomersClient,
        function_customer: CustomerFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send update customer with invalid payload"):
            response = customers_client._request(
                "PUT",
                f"/customers/{function_customer.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"passport_number": "abc"}, id="passport_number_string"),
            pytest.param({"age": "old"}, id="age_string"),
            pytest.param({"passport_number": 9223372036854775808}, id="passport_too_large"),
            pytest.param({"age": -1}, id="age_negative"),
            pytest.param({"age": 4294967296}, id="age_too_large"),
            pytest.param({"first_name": "A" * 21}, id="first_name_too_long"),
            pytest.param({"last_name": "A" * 256}, id="last_name_too_long"),
            pytest.param({"email": "A" * 256}, id="email_too_long"),
            pytest.param({"city": "A" * 256}, id="city_too_long"),
        ],
    )
    def test_partial_update_customer_invalid_payload(
        self,
        customers_client: CustomersClient,
        function_customer: CustomerFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send partial update customer with invalid payload"):
            response = customers_client._request(
                "PATCH",
                f"/customers/{function_customer.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid partial update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_delete_customer_not_found(self, customers_client: CustomersClient):
        with allure.step("Delete non-existent customer"):
            response = customers_client.delete_customer_api(999999999)
        with allure.step("Assert not found or validation error"):
            assert response.status_code in {
                HTTPStatus.NOT_FOUND,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNPROCESSABLE_ENTITY,
            }
