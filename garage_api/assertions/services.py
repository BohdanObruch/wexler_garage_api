from __future__ import annotations

from garage_api.schemas.requests import (
    CreateServiceRequestSchema,
    PartialUpdateServiceRequestSchema,
    UpdateServiceRequestSchema,
)
from garage_api.schemas.responses import ServiceResponseSchema


def assert_create_service_response(
    request: CreateServiceRequestSchema,
    response: ServiceResponseSchema,
) -> None:
    assert response.service_name == request.service_name
    assert response.service_cost_usd == request.service_cost_usd


def assert_update_service_response(
    request: UpdateServiceRequestSchema,
    response: ServiceResponseSchema,
) -> None:
    assert_create_service_response(request, response)


def assert_partial_update_service_response(
    request: PartialUpdateServiceRequestSchema,
    response: ServiceResponseSchema,
) -> None:
    if request.service_name is not None:
        assert response.service_name == request.service_name
    if request.service_cost_usd is not None:
        assert response.service_cost_usd == request.service_cost_usd
