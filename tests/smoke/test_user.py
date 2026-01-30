import allure
from http import HTTPStatus

from garage_api.clients import AuthClient
from garage_api.schemas.requests import TokenLoginRequestSchema
from garage_api.schemas.responses import UserLoginResponseSchema
from garage_api.assertions import assert_status_code, validate_json_schema
from tests.conftest import username, password


class TestUser:
    @allure.tag("smoke")
    def test_user_login(self):
        client = AuthClient()
        request = TokenLoginRequestSchema(username=username, password=password)
        response = client.login_api(request)
        response_data = UserLoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())
