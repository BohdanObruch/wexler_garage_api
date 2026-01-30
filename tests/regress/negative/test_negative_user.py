import allure
import pytest
from http import HTTPStatus

from garage_api.clients import AuthClient
from tests.helpers.negative_assertions import assert_client_error


class TestUserNegative:
    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_all"),
            pytest.param({"username": "user@example.com"}, id="missing_password"),
            pytest.param({"password": "pass"}, id="missing_username"),
            pytest.param({"username": 123, "password": "pass"}, id="username_int"),
            pytest.param({"username": "user@example.com", "password": 123}, id="password_int"),
            pytest.param({"username": "", "password": "pass"}, id="username_empty"),
            pytest.param({"username": "user@example.com", "password": ""}, id="password_empty"),
        ],
    )
    def test_login_missing_or_invalid_fields(self, payload: dict[str, object]) -> None:
        client = AuthClient()
        with allure.step("Send login with invalid payload"):
            response = client._request("POST", "/user/login/", data=payload)
        with allure.step("Assert client error for invalid login payload"):
            assert_client_error(
                response,
                allowed_statuses={
                    HTTPStatus.BAD_REQUEST,
                    HTTPStatus.UNAUTHORIZED,
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                },
            )

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({}, id="missing_all"),
            pytest.param({"refresh": 123}, id="refresh_int"),
            pytest.param({"refresh": ""}, id="refresh_empty"),
        ],
    )
    def test_refresh_missing_or_invalid_fields(self, payload: dict[str, object]) -> None:
        client = AuthClient()
        with allure.step("Send refresh with invalid payload"):
            response = client._request("POST", "/user/login/refresh/", data=payload)
        with allure.step("Assert error for invalid refresh payload"):
            assert response.status_code in {
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNAUTHORIZED,
                HTTPStatus.UNPROCESSABLE_ENTITY,
            }
