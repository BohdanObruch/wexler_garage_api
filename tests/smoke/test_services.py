import allure
import pytest
from garage_api.clients import ServicesClient
from garage_api.schemas.responses import ServicesListResponseSchema
from tests.data.pagination import PAGINATION_PARAMS
from tests.helpers.list_assertions import assert_list_response


class TestServices:
    @allure.tag("smoke")
    @pytest.mark.parametrize("params", PAGINATION_PARAMS)
    def test_services_list(
        self,
        services_client: ServicesClient,
        params: dict[str, int] | None,
    ):
        response = services_client.list_services_api(params=params)
        assert_list_response(response, ServicesListResponseSchema, params=params)
