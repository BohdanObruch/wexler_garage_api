from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

from garage_api.clients import (
    AdministrationClient,
    AuthClient,
    CarEnginesClient,
    CarsClient,
    CustomersClient,
    KitchenClient,
    OperationsClient,
    PaymentsClient,
    RootClient,
    ServicesClient,
)
from garage_api.schemas.requests import (
    CreateCarEngineRequestSchema,
    CreateCarRequestSchema,
    CreateCustomerRequestSchema,
    CreateOperationRequestSchema,
    CreatePaymentRequestSchema,
    CreateServiceRequestSchema,
    TokenLoginRequestSchema,
)
from garage_api.schemas.responses import (
    CarEngineResponseSchema,
    CarResponseSchema,
    CustomerResponseSchema,
    OperationResponseSchema,
    PaymentResponseSchema,
    ServiceResponseSchema,
    UserLoginResponseSchema,
)
from tests.fixtures.types import (
    CarEngineFixture,
    CarFixture,
    CustomerFixture,
    OperationFixture,
    PaymentFixture,
    ServiceFixture,
)

load_dotenv()

username = os.getenv("API_USERNAME")
password = os.getenv("API_PASSWORD")


@pytest.fixture(scope="session")
def token() -> tuple[str, str]:
    client = AuthClient()
    request = TokenLoginRequestSchema(username=username, password=password)
    response = client.login_api(request)
    response_data = UserLoginResponseSchema.model_validate_json(response.text)
    return response_data.access, response_data.refresh


@pytest.fixture()
def access_token(token: tuple[str, str]) -> str:
    return token[0]


@pytest.fixture()
def administration_client(access_token: str) -> AdministrationClient:
    return AdministrationClient(access_token)


@pytest.fixture()
def cars_client(access_token: str) -> CarsClient:
    return CarsClient(access_token)


@pytest.fixture()
def car_engines_client(access_token: str) -> CarEnginesClient:
    return CarEnginesClient(access_token)


@pytest.fixture()
def customers_client(access_token: str) -> CustomersClient:
    return CustomersClient(access_token)


@pytest.fixture()
def kitchen_client(access_token: str) -> KitchenClient:
    return KitchenClient(access_token)


@pytest.fixture()
def operations_client(access_token: str) -> OperationsClient:
    return OperationsClient(access_token)


@pytest.fixture()
def payments_client(access_token: str) -> PaymentsClient:
    return PaymentsClient(access_token)


@pytest.fixture()
def root_client(access_token: str) -> RootClient:
    return RootClient(access_token)


@pytest.fixture()
def services_client(access_token: str) -> ServicesClient:
    return ServicesClient(access_token)


@pytest.fixture()
def function_customer(customers_client: CustomersClient) -> CustomerFixture:
    request = CreateCustomerRequestSchema()
    response = customers_client.create_customer_api(request)
    response_data = CustomerResponseSchema.model_validate_json(response.text)
    return CustomerFixture(request=request, response=response_data)


@pytest.fixture()
def function_car_engine(car_engines_client: CarEnginesClient) -> CarEngineFixture:
    request = CreateCarEngineRequestSchema()
    response = car_engines_client.create_car_engine_api(request)
    response_data = CarEngineResponseSchema.model_validate_json(response.text)
    return CarEngineFixture(request=request, response=response_data)


@pytest.fixture()
def function_service(services_client: ServicesClient) -> ServiceFixture:
    request = CreateServiceRequestSchema()
    response = services_client.create_service_api(request)
    response_data = ServiceResponseSchema.model_validate_json(response.text)
    return ServiceFixture(request=request, response=response_data)


@pytest.fixture()
def function_payment(payments_client: PaymentsClient) -> PaymentFixture:
    request = CreatePaymentRequestSchema()
    response = payments_client.create_payment_api(request)
    response_data = PaymentResponseSchema.model_validate_json(response.text)
    return PaymentFixture(request=request, response=response_data)


@pytest.fixture()
def function_car(
    cars_client: CarsClient,
    function_customer: CustomerFixture,
) -> CarFixture:
    request = CreateCarRequestSchema(car_owner=function_customer.response.id)
    response = cars_client.create_car_api(request)
    response_data = CarResponseSchema.model_validate_json(response.text)
    return CarFixture(request=request, response=response_data)


@pytest.fixture()
def function_operation(
    operations_client: OperationsClient,
    function_car: CarFixture,
    function_service: ServiceFixture,
    function_payment: PaymentFixture,
) -> OperationFixture:
    request = CreateOperationRequestSchema(
        car=function_car.response.id,
        service=function_service.response.id,
        payment=function_payment.response.id,
    )
    response = operations_client.create_operation_api(request)
    response_data = OperationResponseSchema.model_validate_json(response.text)
    return OperationFixture(request=request, response=response_data)
