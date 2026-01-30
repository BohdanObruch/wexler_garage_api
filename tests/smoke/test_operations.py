import allure
import pytest
from garage_api.clients import OperationsClient
from garage_api.schemas.responses import OperationsListResponseSchema
from tests.data.pagination import PAGINATION_PARAMS
from tests.helpers.list_assertions import assert_list_response


class TestOperations:
    @allure.tag("smoke")
    @pytest.mark.parametrize("params", PAGINATION_PARAMS)
    def test_operations_list(
        self,
        operations_client: OperationsClient,
        params: dict[str, int] | None,
    ):
        response = operations_client.list_operations_api(params=params)
        assert_list_response(response, OperationsListResponseSchema, params=params)
