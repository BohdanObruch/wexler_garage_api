import allure
import pytest
from garage_api.clients import CustomersClient
from garage_api.schemas.responses import CustomersListResponseSchema
from tests.data.pagination import PAGINATION_PARAMS
from tests.helpers.list_assertions import assert_list_response


class TestCustomers:
    @allure.tag("smoke")
    @pytest.mark.parametrize("params", PAGINATION_PARAMS)
    def test_list_customers(
        self,
        customers_client: CustomersClient,
        params: dict[str, int] | None,
    ):
        response = customers_client.list_customers_api(params=params)
        assert_list_response(response, CustomersListResponseSchema, params=params)
