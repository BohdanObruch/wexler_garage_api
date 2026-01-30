import allure
from http import HTTPStatus

from garage_api.clients import OperationsClient
from garage_api.helpers import app
from garage_api.schemas.requests import (
    CreateOperationRequestSchema,
    OperationInitRequestSchema,
    PartialUpdateOperationRequestSchema,
    UpdateOperationRequestSchema,
)
from garage_api.schemas.responses import (
    OperationDetailsResponseSchema,
    OperationResponseSchema,
)
from garage_api.assertions import (
    assert_create_operation_response,
    assert_datetime_format,
    assert_partial_update_operation_response,
    assert_status_code,
    assert_update_operation_response,
    validate_json_schema,
)
from tests.fixtures.types import (
    CarFixture,
    OperationFixture,
    PaymentFixture,
    ServiceFixture,
)


class TestOperations:
    @allure.tag("regress")
    def test_create_operations(
        self,
        operations_client: OperationsClient,
        function_car: CarFixture,
        function_service: ServiceFixture,
        function_payment: PaymentFixture,
    ):
        request = CreateOperationRequestSchema(
            car=function_car.response.id,
            service=function_service.response.id,
            payment=function_payment.response.id,
        )
        response = operations_client.create_operation_api(request)
        response_data = OperationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_operation_response(request, response_data)
        assert_datetime_format(response_data.operation_timestamp, "%d/%m/%Y %H:%M:%S")

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_init_operations(
        self, operations_client: OperationsClient, token: tuple[str, str]
    ):
        random_data = app.operations.random_operations_init(token)
        if random_data is None:
            return
        request = OperationInitRequestSchema(
            plate_number=random_data[0],
            service_name=random_data[1],
        )
        response = operations_client.init_operation_api(request)
        response_data = OperationDetailsResponseSchema.model_validate_json(
            response.text
        )

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.car.plate_number == request.plate_number
        assert response_data.service.service_name == request.service_name
        assert response_data.operation_status != "in progress"

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_details_by_random_operations(
        self,
        operations_client: OperationsClient,
        function_operation: OperationFixture,
    ):
        response = operations_client.get_operation_api(function_operation.response.id)
        response_data = OperationDetailsResponseSchema.model_validate_json(
            response.text
        )

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.id == function_operation.response.id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_update_operations(
        self,
        operations_client: OperationsClient,
        function_operation: OperationFixture,
    ):
        request = UpdateOperationRequestSchema(
            car=function_operation.request.car,
            service=function_operation.request.service,
            payment=function_operation.request.payment,
        )
        response = operations_client.update_operation_api(
            function_operation.response.id, request
        )
        response_data = OperationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_operation_response(request, response_data)
        assert_datetime_format(response_data.operation_timestamp, "%d/%m/%Y %H:%M:%S")

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_partial_update_operations(
        self,
        operations_client: OperationsClient,
        function_operation: OperationFixture,
    ):
        request = PartialUpdateOperationRequestSchema(
            final_price=function_operation.request.final_price,
            operation_status=function_operation.request.operation_status,
        )
        response = operations_client.partial_update_operation_api(
            function_operation.response.id, request
        )
        response_data = OperationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_partial_update_operation_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_delete_operations(
        self, operations_client: OperationsClient, function_operation: OperationFixture
    ):
        response = operations_client.delete_operation_api(
            function_operation.response.id
        )

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)
        assert response.text == ""

    @allure.tag("regress")
    def test_finished_operations(
        self, operations_client: OperationsClient, token: tuple[str, str]
    ):
        random_id = app.operations.operations_is_not_finish(token)
        if random_id is None:
            return

        response = operations_client.finish_operation_api(random_id)
        response_data = OperationDetailsResponseSchema.model_validate_json(
            response.text
        )

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert response_data.operation_status == "finished"
        assert response_data.id == random_id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_operations_in_progress(
        self, operations_client: OperationsClient, token: tuple[str, str]
    ):
        random_id = app.operations.operations_is_in_progress(token)
        if random_id is None:
            return

        response = operations_client.mark_in_progress_api(random_id)
        if response.status_code != HTTPStatus.OK:
            return

        response_data = OperationDetailsResponseSchema.model_validate_json(
            response.text
        )
        assert response_data.operation_status == "in progress"
        assert response_data.id == random_id

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag("regress")
    def test_stop_operations(
        self, operations_client: OperationsClient, token: tuple[str, str]
    ):
        random_id = app.operations.random_operations_id(token)
        if random_id is None:
            return

        response = operations_client.stop_operation_api(random_id)
        if response.status_code != HTTPStatus.OK:
            return

        response_data = OperationDetailsResponseSchema.model_validate_json(
            response.text
        )
        assert response_data.operation_status == "stopped"
        assert response_data.id == random_id

        validate_json_schema(response.json(), response_data.model_json_schema())
