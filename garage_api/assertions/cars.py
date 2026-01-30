from __future__ import annotations

import allure
from garage_api.schemas.requests import (
    CreateCarRequestSchema,
    PartialUpdateCarRequestSchema,
    UpdateCarRequestSchema,
)
from garage_api.schemas.responses import CarResponseSchema


def assert_create_car_response(
    request: CreateCarRequestSchema, response: CarResponseSchema
) -> None:
    with allure.step("Check create car response fields"):
        assert response.plate_number == request.plate_number
        assert response.brand == request.brand
        assert response.model == request.model
        assert response.engine_number == request.engine_number
        assert response.car_owner == request.car_owner


def assert_update_car_response(
    request: UpdateCarRequestSchema, response: CarResponseSchema
) -> None:
    with allure.step("Check update car response fields"):
        assert_create_car_response(request, response)


def assert_partial_update_car_response(
    request: PartialUpdateCarRequestSchema,
    response: CarResponseSchema,
) -> None:
    with allure.step("Check partial update car response fields"):
        if request.plate_number is not None:
            assert response.plate_number == request.plate_number
        if request.brand is not None:
            assert response.brand == request.brand
        if request.model is not None:
            assert response.model == request.model
        if request.engine_number is not None:
            assert response.engine_number == request.engine_number
        if request.car_owner is not None:
            assert response.car_owner == request.car_owner
