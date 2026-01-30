from __future__ import annotations

from dataclasses import dataclass

from garage_api.schemas.requests import (
    CreateCarEngineRequestSchema,
    CreateCarRequestSchema,
    CreateCustomerRequestSchema,
    CreateOperationRequestSchema,
    CreatePaymentRequestSchema,
    CreateServiceRequestSchema,
)
from garage_api.schemas.responses import (
    CarEngineResponseSchema,
    CarResponseSchema,
    CustomerResponseSchema,
    OperationResponseSchema,
    PaymentResponseSchema,
    ServiceResponseSchema,
)


@dataclass
class CarEngineFixture:
    request: CreateCarEngineRequestSchema
    response: CarEngineResponseSchema


@dataclass
class CustomerFixture:
    request: CreateCustomerRequestSchema
    response: CustomerResponseSchema


@dataclass
class CarFixture:
    request: CreateCarRequestSchema
    response: CarResponseSchema


@dataclass
class ServiceFixture:
    request: CreateServiceRequestSchema
    response: ServiceResponseSchema


@dataclass
class PaymentFixture:
    request: CreatePaymentRequestSchema
    response: PaymentResponseSchema


@dataclass
class OperationFixture:
    request: CreateOperationRequestSchema
    response: OperationResponseSchema
