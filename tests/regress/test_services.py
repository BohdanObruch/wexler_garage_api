import allure
from http import HTTPStatus

from garage_api.clients import ServicesClient
from garage_api.schemas.requests import (
    CreateServiceRequestSchema,
    DiscountRequestSchema,
    PartialUpdateServiceRequestSchema,
    UpdateServiceRequestSchema,
)
from garage_api.schemas.responses import (
    DiscountServiceResponseSchema,
    ServiceResponseSchema,
)
from garage_api.assertions import (
    assert_create_service_response,
    assert_partial_update_service_response,
    assert_status_code,
    assert_update_service_response,
    validate_json_schema,
)
from tests.fixtures.types import ServiceFixture


class TestServices:
    @allure.tag("regress")
    def test_create_services_post(self, services_client: ServicesClient):
        request = CreateServiceRequestSchema()
        response = services_client.create_service_api(request)
        response_data = ServiceResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_service_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_apply_discounts_v2_services(
        self,
        services_client: ServicesClient,
        function_service: ServiceFixture,
    ):
        request = DiscountRequestSchema()
        response = services_client.apply_discount_v2_api(
            function_service.response.id, request
        )
        response_data = DiscountServiceResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.root[0].id == function_service.response.id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_create_services_put(self, services_client: ServicesClient):
        request = CreateServiceRequestSchema()
        response = services_client.create_service_put_api(request)
        response_data = ServiceResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_service_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_details_by_random_service_id(
        self,
        services_client: ServicesClient,
        function_service: ServiceFixture,
    ):
        response = services_client.get_service_api(function_service.response.id)
        response_data = ServiceResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.id == function_service.response.id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_update_services(
        self, services_client: ServicesClient, function_service: ServiceFixture
    ):
        request = UpdateServiceRequestSchema()
        response = services_client.update_service_api(
            function_service.response.id, request
        )
        response_data = ServiceResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_service_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_partial_update_services(
        self,
        services_client: ServicesClient,
        function_service: ServiceFixture,
    ):
        request = PartialUpdateServiceRequestSchema(
            service_cost_usd=function_service.request.service_cost_usd,
        )
        response = services_client.partial_update_service_api(
            function_service.response.id, request
        )
        response_data = ServiceResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_partial_update_service_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_delete_services(
        self, services_client: ServicesClient, function_service: ServiceFixture
    ):
        response = services_client.delete_service_api(function_service.response.id)

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)
        assert response.text == ""

    @allure.tag("regress")
    def test_apply_discounts_services(
        self,
        services_client: ServicesClient,
        function_service: ServiceFixture,
    ):
        request = DiscountRequestSchema()
        response = services_client.apply_discount_api(
            function_service.response.id, request
        )
        response_data = DiscountServiceResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.root[0].id == function_service.response.id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_apply_discounts_for_all_services(self, services_client: ServicesClient):
        request = DiscountRequestSchema()
        response = services_client.apply_discounts_api(request)
        response_data = DiscountServiceResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())
