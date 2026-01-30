import allure
import pytest
from http import HTTPStatus

import requests

from garage_api.clients import ServicesClient
from tests.data.invalid_params import EDGE_PAGINATION_PARAMS, INVALID_PAGINATION_PARAMS
from tests.helpers.negative_assertions import (
    assert_client_or_server_error,
    assert_not_found_or_error,
    assert_not_server_error,
)
from tests.fixtures.types import ServiceFixture


class TestServicesNegative:
    @allure.tag("regress")
    @pytest.mark.parametrize("params", INVALID_PAGINATION_PARAMS)
    def test_list_services_invalid_pagination(
        self,
        services_client: ServicesClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid pagination"):
            response = services_client.list_services_api(params=params)
        with allure.step("Assert no server error for pagination validation"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize("params", EDGE_PAGINATION_PARAMS)
    def test_list_services_edge_pagination(
        self,
        services_client: ServicesClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with edge pagination"):
            response = services_client.list_services_api(params=params)
        with allure.step("Assert no server error for edge pagination"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"service_cost_usd": "free"}, id="service_cost_usd_string"),
            pytest.param({"service_name": 123}, id="service_name_int"),
        ],
    )
    def test_list_services_invalid_filters(
        self,
        services_client: ServicesClient,
        params: dict[str, object],
    ):
        with allure.step("Send request with invalid filters"):
            response = services_client.list_services_api(params=params)
        with allure.step("Assert no server error for invalid filters"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"service_cost_usd": "free"}, id="service_cost_usd_string"),
            pytest.param({"service_name": 123}, id="service_name_int"),
            pytest.param({"service_name": ""}, id="service_name_empty"),
            pytest.param({"service_name": "A" * 31}, id="service_name_too_long"),
        ],
    )
    def test_create_service_invalid_payload(
        self,
        services_client: ServicesClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create service with invalid payload"):
            response = services_client._request("POST", "/services/", data=payload)
        with allure.step("Assert no server error for invalid create payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"service_cost_usd": "free"}, id="service_cost_usd_string"),
            pytest.param({"service_name": 123}, id="service_name_int"),
            pytest.param({"service_name": ""}, id="service_name_empty"),
            pytest.param({"service_name": "A" * 31}, id="service_name_too_long"),
        ],
    )
    def test_create_service_put_invalid_payload(
        self,
        services_client: ServicesClient,
        payload: dict[str, object],
    ):
        with allure.step("Send create service (PUT) with invalid payload"):
            response = services_client._request("PUT", "/services/put/", data=payload)
        with allure.step("Assert no server error for invalid create PUT payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_get_service_not_found(self, services_client: ServicesClient):
        with allure.step("Request non-existent service"):
            response = services_client.get_service_api(999999999)
        with allure.step("Assert not found or client error"):
            assert_not_found_or_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"service_cost_usd": "free"}, id="service_cost_usd_string"),
            pytest.param({"service_name": 123}, id="service_name_int"),
            pytest.param({"service_name": ""}, id="service_name_empty"),
            pytest.param({"service_name": "A" * 31}, id="service_name_too_long"),
        ],
    )
    def test_update_service_invalid_payload(
        self,
        services_client: ServicesClient,
        function_service: ServiceFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send update service with invalid payload"):
            response = services_client._request(
                "PUT",
                f"/services/{function_service.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"service_cost_usd": "free"}, id="service_cost_usd_string"),
            pytest.param({"service_name": 123}, id="service_name_int"),
            pytest.param({"service_name": ""}, id="service_name_empty"),
            pytest.param({"service_name": "A" * 31}, id="service_name_too_long"),
        ],
    )
    def test_partial_update_service_invalid_payload(
        self,
        services_client: ServicesClient,
        function_service: ServiceFixture,
        payload: dict[str, object],
    ):
        with allure.step("Send partial update service with invalid payload"):
            response = services_client._request(
                "PATCH",
                f"/services/{function_service.response.id}/",
                data=payload,
            )
        with allure.step("Assert no server error for invalid partial update payload"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_delete_service_not_found(self, services_client: ServicesClient):
        with allure.step("Delete non-existent service"):
            response = services_client.delete_service_api(999999999)
        with allure.step("Assert not found or validation error"):
            assert response.status_code in {
                HTTPStatus.NOT_FOUND,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNPROCESSABLE_ENTITY,
            }

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"discount": "ten"}, id="discount_string"),
            pytest.param({"discount": 0}, id="discount_zero"),
        ],
    )
    def test_apply_discount_invalid_params(
        self,
        services_client: ServicesClient,
        function_service: ServiceFixture,
        params: dict[str, object],
    ):
        with allure.step("Send apply_discount with invalid params"):
            response = services_client._request(
                "GET",
                f"/services/{function_service.response.id}/apply_discount/",
                params=params,
            )
        with allure.step("Assert client or server error for invalid discount"):
            assert_client_or_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"discount": "ten"}, id="discount_string"),
        ],
    )
    def test_apply_discount_v2_invalid_params(
        self,
        services_client: ServicesClient,
        function_service: ServiceFixture,
        params: dict[str, object],
    ):
        with allure.step("Send apply_discount_v2 with invalid params"):
            response = services_client._request(
                "GET",
                f"/services/{function_service.response.id}/apply_discount_v2/",
                params=params,
            )
        with allure.step("Assert client or server error for invalid discount v2"):
            assert_client_or_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize(
        "params",
        [
            pytest.param({"discount": "ten"}, id="discount_string"),
            pytest.param({"version": "v2"}, id="version_string"),
            pytest.param({"service_cost_usd": "free"}, id="service_cost_usd_string"),
            pytest.param({"service_name": 123}, id="service_name_int"),
        ],
    )
    def test_apply_discounts_invalid_params(
        self,
        services_client: ServicesClient,
        params: dict[str, object],
    ):
        with allure.step("Send apply_discounts with invalid params"):
            try:
                response = services_client._request(
                    "GET",
                    "/services/apply_discounts/",
                    params=params,
                )
            except requests.exceptions.ConnectionError:
                pytest.skip("Service host not reachable for apply_discounts")
        with allure.step("Assert client or server error for invalid apply_discounts params"):
            assert_client_or_server_error(response)

    @allure.tag("regress")
    @pytest.mark.parametrize("params", INVALID_PAGINATION_PARAMS)
    def test_apply_discounts_invalid_pagination(
        self,
        services_client: ServicesClient,
        params: dict[str, object],
    ):
        with allure.step("Send apply_discounts with invalid pagination"):
            response = services_client._request(
                "GET",
                "/services/apply_discounts/",
                params=params,
            )
        with allure.step("Assert client or server error for invalid pagination"):
            assert_client_or_server_error(response)
