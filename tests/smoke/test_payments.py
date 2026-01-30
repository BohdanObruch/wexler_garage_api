import allure
import pytest
from garage_api.clients import PaymentsClient
from garage_api.schemas.responses import PaymentsListResponseSchema
from tests.data.pagination import PAGINATION_PARAMS
from tests.helpers.list_assertions import assert_list_response


class TestPayments:
    @allure.tag("smoke")
    @pytest.mark.parametrize("params", PAGINATION_PARAMS)
    def test_payments_list(
        self,
        payments_client: PaymentsClient,
        params: dict[str, int] | None,
    ):
        response = payments_client.list_payments_api(params=params)
        assert_list_response(response, PaymentsListResponseSchema, params=params)
