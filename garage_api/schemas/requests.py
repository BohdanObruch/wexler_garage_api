from __future__ import annotations

import random
from typing import Optional

from faker import Faker
from pydantic import BaseModel, ConfigDict, Field

fake = Faker()


class ApiRequestModel(BaseModel):
    model_config = ConfigDict(extra="ignore")


def _random_plate_number() -> str:
    return "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(8)
    )


def _random_engine_number() -> str:
    length = random.randint(10, 17)
    return "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(length)
    )


def _random_service_name() -> str:
    return fake.sentence(nb_words=2)


def _random_service_cost() -> float:
    return round(random.uniform(10.00, 99.00), 2)


def _random_discount() -> int:
    return random.randint(1, 99)


def _random_amount() -> str:
    return f"{round(random.uniform(10.00, 99.00), 2):.2f}"


def _random_currency() -> str:
    return random.choice(["USD", "TRY", "EUR", "GBP", "CNY"])


def _random_invoice_id() -> str:
    return "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(10)
    )


def _random_transaction_id() -> str:
    return "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(10)
    )


def _random_signature() -> str:
    return "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(15)
    )


def _random_payment_status() -> str:
    return random.choice(["SUCCESS", "IN PROGRESS", "FAILED"])


def _random_price() -> str:
    return f"{round(random.uniform(10.00, 99.00), 2):.2f}"


def _random_origin() -> str:
    origin = fake.country()
    while len(origin) > 30:
        origin = fake.country()
    return origin


class TokenLoginRequestSchema(ApiRequestModel):
    username: str
    password: str


class TokenRefreshRequestSchema(ApiRequestModel):
    refresh: str


class CreateCarEngineRequestSchema(ApiRequestModel):
    engine_number: str = Field(default_factory=_random_engine_number)
    volume: float = Field(default_factory=lambda: round(random.uniform(1.0, 9.0), 1))
    origin: Optional[str] = Field(default_factory=_random_origin)
    production_year: Optional[int] = Field(default_factory=lambda: int(fake.year()))


class UpdateCarEngineRequestSchema(CreateCarEngineRequestSchema):
    pass


class PartialUpdateCarEngineRequestSchema(ApiRequestModel):
    engine_number: Optional[str] = None
    volume: Optional[float] = None
    origin: Optional[str] = None
    production_year: Optional[int] = None


class CreateCustomerRequestSchema(ApiRequestModel):
    passport_number: int = Field(
        default_factory=lambda: random.randint(10000000, 99999999)
    )
    first_name: Optional[str] = Field(default_factory=fake.first_name)
    last_name: Optional[str] = Field(default_factory=fake.last_name)
    email: Optional[str] = Field(default_factory=fake.email)
    age: Optional[int] = Field(default_factory=lambda: random.randint(18, 100))
    city: Optional[str] = Field(default_factory=fake.city)


class UpdateCustomerRequestSchema(CreateCustomerRequestSchema):
    pass


class PartialUpdateCustomerRequestSchema(ApiRequestModel):
    passport_number: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None


class CreateCarRequestSchema(ApiRequestModel):
    plate_number: str = Field(default_factory=_random_plate_number)
    brand: Optional[str] = Field(default_factory=fake.company)
    model: Optional[str] = Field(default_factory=fake.street_suffix)
    engine_number: Optional[str] = Field(default_factory=_random_engine_number)
    car_owner: int


class UpdateCarRequestSchema(CreateCarRequestSchema):
    pass


class PartialUpdateCarRequestSchema(ApiRequestModel):
    plate_number: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    engine_number: Optional[str] = None
    car_owner: Optional[int] = None


class CreateServiceRequestSchema(ApiRequestModel):
    service_name: str = Field(default_factory=_random_service_name)
    service_cost_usd: float = Field(default_factory=_random_service_cost)


class UpdateServiceRequestSchema(CreateServiceRequestSchema):
    pass


class PartialUpdateServiceRequestSchema(ApiRequestModel):
    service_name: Optional[str] = None
    service_cost_usd: Optional[float] = None


class DiscountRequestSchema(ApiRequestModel):
    discount: int = Field(default_factory=_random_discount)


class CreatePaymentRequestSchema(ApiRequestModel):
    amount: str = Field(default_factory=_random_amount)
    currency: str = Field(default_factory=_random_currency)
    InvId: str = Field(default_factory=_random_invoice_id)
    trsid: str = Field(default_factory=_random_transaction_id)
    custom: str = Field(default_factory=lambda: fake.sentence(nb_words=2))
    signature: str = Field(default_factory=_random_signature)
    status: str = Field(default_factory=_random_payment_status)


class UpdatePaymentRequestSchema(CreatePaymentRequestSchema):
    pass


class PartialUpdatePaymentRequestSchema(ApiRequestModel):
    status: Optional[str] = None


class PaymentSuccessRequestSchema(ApiRequestModel):
    amount: str
    currency: str
    InvId: str
    trsid: str
    custom: str
    signature: str
    status: str


class CreateOperationRequestSchema(ApiRequestModel):
    final_price: str = Field(default_factory=_random_price)
    operation_status: Optional[str] = Field(default_factory=lambda: "started")
    car: int
    service: int
    payment: Optional[int]


class UpdateOperationRequestSchema(CreateOperationRequestSchema):
    pass


class PartialUpdateOperationRequestSchema(ApiRequestModel):
    final_price: Optional[str] = None
    operation_status: Optional[str] = None


class OperationInitRequestSchema(ApiRequestModel):
    plate_number: str
    service_name: str
