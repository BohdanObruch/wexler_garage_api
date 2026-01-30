import allure
from http import HTTPStatus

from garage_api.clients import CarEnginesClient
from garage_api.schemas.requests import (
    CreateCarEngineRequestSchema,
    PartialUpdateCarEngineRequestSchema,
    UpdateCarEngineRequestSchema,
)
from garage_api.schemas.responses import CarEngineResponseSchema
from garage_api.assertions import (
    assert_create_car_engine_response,
    assert_partial_update_car_engine_response,
    assert_status_code,
    assert_update_car_engine_response,
    validate_json_schema,
)
from tests.fixtures.types import CarEngineFixture


class TestCarEngines:
    @allure.tag("regress")
    def test_create_car_engines_post(self, car_engines_client: CarEnginesClient):
        request = CreateCarEngineRequestSchema()
        response = car_engines_client.create_car_engine_api(request)
        response_data = CarEngineResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_car_engine_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_create_car_engines_put(self, car_engines_client: CarEnginesClient):
        request = CreateCarEngineRequestSchema()
        response = car_engines_client.create_car_engine_put_api(request)
        response_data = CarEngineResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_car_engine_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_details_by_random_engine_number(
        self,
        car_engines_client: CarEnginesClient,
        function_car_engine: CarEngineFixture,
    ):
        response = car_engines_client.get_car_engine_api(
            function_car_engine.response.id
        )
        response_data = CarEngineResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.id == function_car_engine.response.id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_update_car_engines(
        self,
        car_engines_client: CarEnginesClient,
        function_car_engine: CarEngineFixture,
    ):
        request = UpdateCarEngineRequestSchema()
        response = car_engines_client.update_car_engine_api(
            function_car_engine.response.id, request
        )
        response_data = CarEngineResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_car_engine_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_partial_update_car_engines(
        self,
        car_engines_client: CarEnginesClient,
        function_car_engine: CarEngineFixture,
    ):
        request = PartialUpdateCarEngineRequestSchema(
            engine_number=function_car_engine.request.engine_number,
            volume=function_car_engine.request.volume,
        )
        response = car_engines_client.partial_update_car_engine_api(
            function_car_engine.response.id,
            request,
        )
        response_data = CarEngineResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_partial_update_car_engine_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_delete_car_engines(
        self,
        car_engines_client: CarEnginesClient,
        function_car_engine: CarEngineFixture,
    ):
        response = car_engines_client.delete_car_engine_api(
            function_car_engine.response.id
        )

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)
        assert response.text == ""
