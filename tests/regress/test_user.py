import allure
import pytest
from faker import Faker
from http import HTTPStatus

from garage_api.clients import AuthClient
from garage_api.schemas.requests import (
    TokenLoginRequestSchema,
    TokenRefreshRequestSchema,
)
from garage_api.schemas.responses import RefreshTokenResponseSchema
from garage_api.assertions import assert_status_code, validate_json_schema

fake = Faker()

invalid_login_test_data = [
    # Username equivalence classes
    pytest.param(fake.email(), fake.password(length=10), id="unregistered_valid_email"),
    pytest.param(
        fake.user_name(), fake.password(length=10), id="username_without_at_symbol"
    ),
    pytest.param("invalid@", fake.password(length=10), id="missing_domain"),
    pytest.param("@domain.com", fake.password(length=10), id="missing_local_part"),
    pytest.param("user@@domain.com", fake.password(length=10), id="double_at"),
    pytest.param(
        "user name@domain.com", fake.password(length=10), id="username_with_space"
    ),
    # Password equivalence classes
    pytest.param(fake.email(), "", id="empty_password"),
    pytest.param(fake.email(), "   ", id="password_only_spaces"),
    pytest.param(fake.email(), "ab", id="password_2_chars"),
    pytest.param(fake.email(), "a" * 256, id="password_256_chars"),
    # Boundary value analysis - empty inputs
    pytest.param("", "", id="both_empty"),
    pytest.param("", fake.password(length=10), id="empty_username"),
    # Boundary value analysis - min/max lengths
    pytest.param("a@b.c", fake.password(length=10), id="min_valid_format"),
    pytest.param(
        f"{'a' * 64}@{'b' * 63}.com", fake.password(length=10), id="max_length_email"
    ),
    # Special characters
    pytest.param(fake.email(), "pass<script>alert(1)</script>", id="xss_in_password"),
    pytest.param(
        fake.email(), "pass'; DROP TABLE users;--", id="sql_injection_password"
    ),
]


class TestUser:
    @allure.tag("regress")
    def test_login_refresh(self, token: tuple[str, str]):
        client = AuthClient()
        request = TokenRefreshRequestSchema(refresh=token[1])
        response = client.refresh_token_api(request)
        response_data = RefreshTokenResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    @pytest.mark.parametrize("username, password", invalid_login_test_data)
    def test_login_invalid_credentials(self, username: str, password: str) -> None:
        client = AuthClient()
        request = TokenLoginRequestSchema(username=username, password=password)
        response = client.login_api(request)

        assert response.status_code in {HTTPStatus.BAD_REQUEST, HTTPStatus.UNAUTHORIZED}
