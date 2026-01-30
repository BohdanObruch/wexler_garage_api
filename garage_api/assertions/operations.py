from __future__ import annotations

import allure
from garage_api.schemas.requests import (
    CreateOperationRequestSchema,
    PartialUpdateOperationRequestSchema,
    UpdateOperationRequestSchema,
)
from garage_api.schemas.responses import OperationResponseSchema


def assert_create_operation_response(
    request: CreateOperationRequestSchema,
    response: OperationResponseSchema,
) -> None:
    with allure.step("Check create operation response fields"):
        assert response.final_price == request.final_price
        assert response.operation_status == request.operation_status
        assert response.car == request.car
        assert response.service == request.service
        assert response.payment == request.payment


def assert_update_operation_response(
    request: UpdateOperationRequestSchema,
    response: OperationResponseSchema,
) -> None:
    with allure.step("Check update operation response fields"):
        assert_create_operation_response(request, response)


def assert_partial_update_operation_response(
    request: PartialUpdateOperationRequestSchema,
    response: OperationResponseSchema,
) -> None:
    with allure.step("Check partial update operation response fields"):
        if request.final_price is not None:
            assert response.final_price == request.final_price
        if request.operation_status is not None:
            assert response.operation_status == request.operation_status
