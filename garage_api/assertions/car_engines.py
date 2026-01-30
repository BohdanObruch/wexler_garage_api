from __future__ import annotations

from garage_api.schemas.requests import (
    CreateCarEngineRequestSchema,
    PartialUpdateCarEngineRequestSchema,
    UpdateCarEngineRequestSchema,
)
from garage_api.schemas.responses import CarEngineResponseSchema


def assert_create_car_engine_response(
    request: CreateCarEngineRequestSchema,
    response: CarEngineResponseSchema,
) -> None:
    assert response.engine_number == request.engine_number
    assert response.volume == request.volume
    assert response.origin == request.origin
    assert response.production_year == request.production_year


def assert_update_car_engine_response(
    request: UpdateCarEngineRequestSchema,
    response: CarEngineResponseSchema,
) -> None:
    assert_create_car_engine_response(request, response)


def assert_partial_update_car_engine_response(
    request: PartialUpdateCarEngineRequestSchema,
    response: CarEngineResponseSchema,
) -> None:
    if request.engine_number is not None:
        assert response.engine_number == request.engine_number
    if request.volume is not None:
        assert response.volume == request.volume
    if request.origin is not None:
        assert response.origin == request.origin
    if request.production_year is not None:
        assert response.production_year == request.production_year
