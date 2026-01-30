from __future__ import annotations

import allure
from garage_api.schemas.requests import (
    CreateCustomerRequestSchema,
    PartialUpdateCustomerRequestSchema,
    UpdateCustomerRequestSchema,
)
from garage_api.schemas.responses import CustomerResponseSchema


def assert_create_customer_response(
    request: CreateCustomerRequestSchema,
    response: CustomerResponseSchema,
) -> None:
    with allure.step("Check create customer response fields"):
        assert response.passport_number == request.passport_number
        assert response.first_name == request.first_name
        assert response.last_name == request.last_name
        assert response.email == request.email
        assert response.age == request.age
        assert response.city == request.city


def assert_update_customer_response(
    request: UpdateCustomerRequestSchema,
    response: CustomerResponseSchema,
) -> None:
    with allure.step("Check update customer response fields"):
        assert_create_customer_response(request, response)


def assert_partial_update_customer_response(
    request: PartialUpdateCustomerRequestSchema,
    response: CustomerResponseSchema,
) -> None:
    with allure.step("Check partial update customer response fields"):
        if request.passport_number is not None:
            assert response.passport_number == request.passport_number
        if request.first_name is not None:
            assert response.first_name == request.first_name
        if request.last_name is not None:
            assert response.last_name == request.last_name
        if request.email is not None:
            assert response.email == request.email
        if request.age is not None:
            assert response.age == request.age
        if request.city is not None:
            assert response.city == request.city
