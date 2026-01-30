import allure
from http import HTTPStatus

from garage_api.clients import CustomersClient
from garage_api.schemas.requests import (
    CreateCustomerRequestSchema,
    PartialUpdateCustomerRequestSchema,
    UpdateCustomerRequestSchema,
)
from garage_api.schemas.responses import CustomerResponseSchema
from garage_api.assertions import (
    assert_create_customer_response,
    assert_partial_update_customer_response,
    assert_status_code,
    assert_update_customer_response,
    validate_json_schema,
)
from tests.fixtures.types import CustomerFixture


class TestCustomers:
    @allure.tag("regress")
    def test_create_customers_post(self, customers_client: CustomersClient):
        request = CreateCustomerRequestSchema()
        response = customers_client.create_customer_api(request)
        response_data = CustomerResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_customer_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_create_customers_put(self, customers_client: CustomersClient):
        request = CreateCustomerRequestSchema()
        response = customers_client.create_customer_put_api(request)
        response_data = CustomerResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_customer_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_details_by_random_customer(
        self,
        customers_client: CustomersClient,
        function_customer: CustomerFixture,
    ):
        response = customers_client.get_customer_api(function_customer.response.id)
        response_data = CustomerResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.id == function_customer.response.id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_update_customer(
        self,
        customers_client: CustomersClient,
        function_customer: CustomerFixture,
    ):
        request = UpdateCustomerRequestSchema()
        response = customers_client.update_customer_api(
            function_customer.response.id, request
        )
        response_data = CustomerResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_customer_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_partial_update_customer(
        self,
        customers_client: CustomersClient,
        function_customer: CustomerFixture,
    ):
        request = PartialUpdateCustomerRequestSchema(
            passport_number=function_customer.request.passport_number,
        )
        response = customers_client.partial_update_customer_api(
            function_customer.response.id, request
        )
        response_data = CustomerResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_partial_update_customer_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_delete_customer(
        self,
        customers_client: CustomersClient,
        function_customer: CustomerFixture,
    ):
        response = customers_client.delete_customer_api(function_customer.response.id)
        if response.status_code != HTTPStatus.NO_CONTENT:
            assert (
                "Cannot delete some instances of model 'Customer' because they are referenced through restricted foreign keys"
                in response.text
            )
            return

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)
        assert response.text == ""
