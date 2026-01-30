import allure
import pytest
from http import HTTPStatus

from garage_api.clients import PaymentsClient
from tests.data.invalid_params import EDGE_PAGINATION_PARAMS, INVALID_PAGINATION_PARAMS
from tests.helpers.negative_assertions import (
    assert_not_found_or_error,
    assert_not_server_error,
)
from tests.fixtures.types import PaymentFixture


class TestPaymentsNegative:
    @allure.tag("regress")
    @pytest.mark.parametrize("params", INVALID_PAGINATION_PARAMS)
    def test_list_payments_invalid_pagination(
        self,
        payments_client: PaymentsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid pagination"):
            response = payments_client.list_payments_api(params=params)
        with allure.step("Assert no server error for pagination validation"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize("params", EDGE_PAGINATION_PARAMS)
    def test_list_payments_edge_pagination(
        self,
        payments_client: PaymentsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with edge pagination"):
            response = payments_client.list_payments_api(params=params)
        with allure.step("Assert no server error for edge pagination"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"amount": "cheap"}, id="amount_string"),
            pytest.param({"status": 123}, id="status_int"),
            pytest.param({"currency": 123}, id="currency_int"),
            pytest.param({"timestamp": 123}, id="timestamp_int"),
            pytest.param({"InvId": 123}, id="inv_id_int"),
            pytest.param({"trsid": 123}, id="trsid_int"),
            pytest.param({"custom": 123}, id="custom_int"),
            pytest.param({"signature": 123}, id="signature_int"),
        ],
    )
    def test_list_payments_invalid_filters(
        self,
        payments_client: PaymentsClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid filters"):
            response = payments_client.list_payments_api(params=params)
        with allure.step("Assert no server error for invalid filters"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"status": "UNKNOWN"}, id="status_invalid_enum"),
            pytest.param({"status": ""}, id="status_empty"),
            pytest.param({"amount": 123}, id="amount_int"),
            pytest.param({"currency": 123}, id="currency_int"),
            pytest.param({"currency": ""}, id="currency_empty"),
            pytest.param({"currency": "ABCDE"}, id="currency_too_long"),
            pytest.param({"amount": "free"}, id="amount_not_decimal"),
            pytest.param({"trsid": ""}, id="trsid_empty"),
            pytest.param({"custom": ""}, id="custom_empty"),
            pytest.param({"InvId": "A" * 256}, id="inv_id_too_long"),
            pytest.param({"signature": 123}, id="signature_int"),
        ],
    )
    def test_create_payment_invalid_payload(
        self,
        payments_client: PaymentsClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create payment with invalid payload"):
            response = payments_client._request("POST", "/payments/", data=payload)
        with allure.step("Assert no server error for invalid create payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"status": "UNKNOWN"}, id="status_invalid_enum"),
            pytest.param({"status": ""}, id="status_empty"),
            pytest.param({"amount": 123}, id="amount_int"),
            pytest.param({"currency": ""}, id="currency_empty"),
            pytest.param({"currency": "ABCDE"}, id="currency_too_long"),
            pytest.param({"amount": "free"}, id="amount_not_decimal"),
            pytest.param({"trsid": ""}, id="trsid_empty"),
            pytest.param({"custom": ""}, id="custom_empty"),
        ],
    )
    def test_create_payment_put_invalid_payload(
        self,
        payments_client: PaymentsClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create payment (PUT) with invalid payload"):
            response = payments_client._request("PUT", "/payments/put/", data=payload)
        with allure.step("Assert no server error for invalid create PUT payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_get_payment_not_found(self, payments_client: PaymentsClient):
        with allure.step("Request non-existent payment"):
            response = payments_client.get_payment_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"status": "UNKNOWN"}, id="status_invalid_enum"),
            pytest.param({"status": ""}, id="status_empty"),
            pytest.param({"amount": 123}, id="amount_int"),
            pytest.param({"currency": ""}, id="currency_empty"),
            pytest.param({"currency": "ABCDE"}, id="currency_too_long"),
            pytest.param({"amount": "free"}, id="amount_not_decimal"),
            pytest.param({"trsid": ""}, id="trsid_empty"),
            pytest.param({"custom": ""}, id="custom_empty"),
        ],
    )
    def test_update_payment_invalid_payload(
        self,
        payments_client: PaymentsClient,
        function_payment: PaymentFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send update payment with invalid payload"):
            response = payments_client._request(
                "PUT",
                f"/payments/{function_payment.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"status": "UNKNOWN"}, id="status_invalid_enum"),
            pytest.param({"status": ""}, id="status_empty"),
            pytest.param({"amount": 123}, id="amount_int"),
            pytest.param({"currency": ""}, id="currency_empty"),
            pytest.param({"currency": "ABCDE"}, id="currency_too_long"),
            pytest.param({"amount": "free"}, id="amount_not_decimal"),
            pytest.param({"trsid": ""}, id="trsid_empty"),
            pytest.param({"custom": ""}, id="custom_empty"),
        ],
    )
    def test_partial_update_payment_invalid_payload(
        self,
        payments_client: PaymentsClient,
        function_payment: PaymentFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send partial update payment with invalid payload"):
            response = payments_client._request(
                "PATCH",
                f"/payments/{function_payment.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid partial update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_delete_payment_not_found(self, payments_client: PaymentsClient):
        with allure.step("Delete non-existent payment"):
            response = payments_client.delete_payment_api(999999999)
        with allure.step("Assert not found or validation error"):
            assert response.status_code in {
                HTTPStatus.NOT_FOUND,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNPROCESSABLE_ENTITY,
            }

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"status": "UNKNOWN"}, id="status_invalid_enum"),
            pytest.param({"status": ""}, id="status_empty"),
            pytest.param({"InvId": 123}, id="inv_id_int"),
            pytest.param({}, id="missing_all"),
            pytest.param({"currency": ""}, id="currency_empty"),
            pytest.param({"currency": "ABCDE"}, id="currency_too_long"),
            pytest.param({"amount": "free"}, id="amount_not_decimal"),
            pytest.param({"trsid": ""}, id="trsid_empty"),
            pytest.param({"custom": ""}, id="custom_empty"),
        ],
    )
    def test_success_payment_invalid_payload(
        self,
        payments_client: PaymentsClient,
        payload: dict[str, object],
    ):
        with allure.step("Send payment success with invalid payload"):
            response = payments_client._request(
                "POST", "/payments/success/", data=payload
            )
        with allure.step("Assert no server error for invalid success payload"):
            assert_not_server_error(response)
