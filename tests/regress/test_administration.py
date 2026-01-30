import allure
from http import HTTPStatus

from garage_api.clients import AdministrationClient
from garage_api.schemas.responses import AdministrationResponseSchema
from garage_api.assertions import assert_status_code, validate_json_schema
from tests.conftest import username


class TestAdministration:
    @allure.tag("regress")
    def test_administration(self, administration_client: AdministrationClient):
        response = administration_client.create_dataset_api()
        response_data = AdministrationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert response_data.status == "SUCCESS"
        assert (
            response_data.message == f"Dataset for user {username} created successfully"
        )

        validate_json_schema(response.json(), response_data.model_json_schema())
