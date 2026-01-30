import allure
from http import HTTPStatus

from garage_api.clients import PaymentsClient
from garage_api.helpers import app
from garage_api.schemas.requests import (
    CreatePaymentRequestSchema,
    PartialUpdatePaymentRequestSchema,
    PaymentSuccessRequestSchema,
    UpdatePaymentRequestSchema,
)
from garage_api.schemas.responses import (
    PaymentResponseSchema,
    PaymentsSuccessResponseSchema,
)
from garage_api.assertions import (
    assert_create_payment_response,
    assert_datetime_format,
    assert_partial_update_payment_response,
    assert_status_code,
    assert_update_payment_response,
    validate_json_schema,
)
from tests.fixtures.types import PaymentFixture


class TestPayments:
    @allure.tag("regress")
    def test_create_payments_post(self, payments_client: PaymentsClient):
        request = CreatePaymentRequestSchema()
        response = payments_client.create_payment_api(request)
        response_data = PaymentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_payment_response(request, response_data)
        assert_datetime_format(response_data.timestamp, "%d/%m/%Y %H:%M:%S")

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_create_payments_put(self, payments_client: PaymentsClient):
        request = CreatePaymentRequestSchema()
        response = payments_client.create_payment_put_api(request)
        response_data = PaymentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_payment_response(request, response_data)
        assert_datetime_format(response_data.timestamp, "%d/%m/%Y %H:%M:%S")

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_payments_success(
        self, payments_client: PaymentsClient, token: tuple[str, str]
    ):
        inv_id = app.payments.list_payments(token)
        if inv_id is None:
            return

        random_request = CreatePaymentRequestSchema()
        request = PaymentSuccessRequestSchema(
            amount=random_request.amount,
            currency=random_request.currency,
            InvId=inv_id,
            trsid=random_request.trsid,
            custom=random_request.custom,
            signature=random_request.signature,
            status="SUCCESS",
        )
        response = payments_client.success_payment_api(request)
        response_data = PaymentsSuccessResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.status == "SUCCESS"

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_read_payments(
        self, payments_client: PaymentsClient, function_payment: PaymentFixture
    ):
        response = payments_client.get_payment_api(function_payment.response.id)
        response_data = PaymentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.id == function_payment.response.id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_update_payments(
        self, payments_client: PaymentsClient, function_payment: PaymentFixture
    ):
        request = UpdatePaymentRequestSchema(status="SUCCESS")
        response = payments_client.update_payment_api(
            function_payment.response.id, request
        )
        response_data = PaymentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_payment_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_partial_update_payments(
        self,
        payments_client: PaymentsClient,
        function_payment: PaymentFixture,
    ):
        request = PartialUpdatePaymentRequestSchema(status="SUCCESS")
        response = payments_client.partial_update_payment_api(
            function_payment.response.id, request
        )
        response_data = PaymentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_partial_update_payment_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_delete_payments(
        self, payments_client: PaymentsClient, function_payment: PaymentFixture
    ):
        response = payments_client.delete_payment_api(function_payment.response.id)

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)
        assert response.text == ""
