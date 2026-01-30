import allure
from http import HTTPStatus

from garage_api.clients import KitchenClient
from garage_api.schemas.responses import KitchenResponseSchema
from garage_api.assertions import validate_json_schema

SUCCESS_MESSAGE = "Кофе сварен!"
ERROR_MESSAGES = [
    "Сервер кофе недоступен",
    "Все занято, приходите позже",
    "Кофе тут не наливают (временно), попробуйте снова",
    "Все кофеварки заняты, пейте чай!",
]


class TestKitchen:
    @allure.tag("regress")
    def test_brew_coffee_in_coffee_maker_list(self, kitchen_client: KitchenClient):
        response = kitchen_client.brew_coffee_api()
        response_data = KitchenResponseSchema.model_validate_json(response.text)

        assert "result" in response.json()
        if response.status_code == HTTPStatus.CREATED:
            assert response_data.result == SUCCESS_MESSAGE
        elif response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
            assert response_data.result in ERROR_MESSAGES

        validate_json_schema(response.json(), response_data.model_json_schema())
