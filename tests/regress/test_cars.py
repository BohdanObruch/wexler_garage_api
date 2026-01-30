import allure
from http import HTTPStatus

from garage_api.clients import CarsClient
from garage_api.schemas.requests import (
    CreateCarRequestSchema,
    PartialUpdateCarRequestSchema,
    UpdateCarRequestSchema,
)
from garage_api.schemas.responses import CarInfoResponseSchema, CarResponseSchema
from garage_api.assertions import (
    assert_create_car_response,
    assert_partial_update_car_response,
    assert_status_code,
    assert_update_car_response,
    validate_json_schema,
)
from tests.fixtures.types import CarFixture, CustomerFixture


class TestCars:
    @allure.tag("regress")
    def test_create_cars_post(
        self, cars_client: CarsClient, function_customer: CustomerFixture
    ):
        request = CreateCarRequestSchema(car_owner=function_customer.response.id)
        response = cars_client.create_car_api(request)
        response_data = CarResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_car_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_create_cars_put(
        self, cars_client: CarsClient, function_customer: CustomerFixture
    ):
        request = CreateCarRequestSchema(car_owner=function_customer.response.id)
        response = cars_client.create_car_put_api(request)
        response_data = CarResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_car_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_details_by_random_car(
        self, cars_client: CarsClient, function_car: CarFixture
    ):
        response = cars_client.get_car_api(function_car.response.id)
        response_data = CarInfoResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.id == function_car.response.id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_update_cars(self, cars_client: CarsClient, function_car: CarFixture):
        request = UpdateCarRequestSchema(car_owner=function_car.request.car_owner)
        response = cars_client.update_car_api(function_car.response.id, request)
        response_data = CarResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_car_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_partial_update_cars(
        self, cars_client: CarsClient, function_car: CarFixture
    ):
        request = PartialUpdateCarRequestSchema(
            plate_number=function_car.request.plate_number,
            model=function_car.request.model,
            car_owner=function_car.request.car_owner,
        )
        response = cars_client.partial_update_car_api(function_car.response.id, request)
        response_data = CarResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_partial_update_car_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_delete_cars(self, cars_client: CarsClient, function_car: CarFixture):
        response = cars_client.delete_car_api(function_car.response.id)

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)
        assert response.content == b""
