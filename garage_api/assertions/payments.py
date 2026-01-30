from __future__ import annotations

import allure
from garage_api.schemas.requests import (
    CreatePaymentRequestSchema,
    PartialUpdatePaymentRequestSchema,
    UpdatePaymentRequestSchema,
)
from garage_api.schemas.responses import PaymentResponseSchema


def assert_create_payment_response(
    request: CreatePaymentRequestSchema,
    response: PaymentResponseSchema,
) -> None:
    with allure.step("Check create payment response fields"):
        assert response.amount == request.amount
        assert response.currency == request.currency
        assert response.InvId == request.InvId
        assert response.trsid == request.trsid
        assert response.custom == request.custom
        assert response.signature == request.signature
        assert response.status == request.status


def assert_update_payment_response(
    request: UpdatePaymentRequestSchema,
    response: PaymentResponseSchema,
) -> None:
    with allure.step("Check update payment response fields"):
        assert_create_payment_response(request, response)


def assert_partial_update_payment_response(
    request: PartialUpdatePaymentRequestSchema,
    response: PaymentResponseSchema,
) -> None:
    with allure.step("Check partial update payment response fields"):
        if request.status is not None:
            assert response.status == request.status
