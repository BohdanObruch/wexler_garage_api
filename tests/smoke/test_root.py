import allure
from http import HTTPStatus

from garage_api.clients import RootClient
from garage_api.schemas.responses import RootResponseSchema
from garage_api.assertions import assert_status_code, validate_json_schema


class TestRoot:
    @allure.tag("smoke")
    def test_root_list(self, root_client: RootClient):
        response = root_client.root_api()
        response_data = RootResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert "/cars/" in response_data.cars
        assert "/customers/" in response_data.customers
        assert "/car_engines/" in response_data.car_engines
        assert "/operations/" in response_data.operations
        assert "/services/" in response_data.services
        assert "/payments/" in response_data.payments

        validate_json_schema(response.json(), response_data.model_json_schema())
