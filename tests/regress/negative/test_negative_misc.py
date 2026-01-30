import allure

from garage_api.clients import AdministrationClient, KitchenClient, RootClient
from tests.helpers.negative_assertions import assert_not_server_error


class TestMiscNegative:
    @allure.tag("regress")
    def test_root_with_unexpected_params(self) -> None:
        client = RootClient()
        with allure.step("Send root request with unexpected query params"):
            response = client._request("GET", "/root/", params={"unexpected": "value"})
        with allure.step("Assert no server error for unexpected params"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_create_dataset_with_unexpected_params(self) -> None:
        client = AdministrationClient()
        with allure.step("Send create_dataset request with unexpected query params"):
            response = client._request(
                "GET", "/administration/create_dataset", params={"limit": "one"}
            )
        with allure.step("Assert no server error for unexpected params"):
            assert_not_server_error(response)

    @allure.tag("regress")
    def test_brew_coffee_with_unexpected_params(self) -> None:
        client = KitchenClient()
        with allure.step("Send brew_coffee request with unexpected query params"):
            response = client._request(
                "GET",
                "/kitchen/brew_coffee_in_coffee_maker",
                params={"brew": "now"},
            )
        with allure.step("Assert no server error for unexpected params"):
            assert_not_server_error(response)
