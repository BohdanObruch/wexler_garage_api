from __future__ import annotations

from typing import Optional, Union

from pydantic import BaseModel, ConfigDict, RootModel


class ApiModel(BaseModel):
    model_config = ConfigDict(extra="ignore")


class Administration(ApiModel):
    status: str
    message: str


class UserLogin(ApiModel):
    refresh: str
    access: str


class RefreshToken(ApiModel):
    access: str


class CarEngine(ApiModel):
    id: int
    engine_number: str
    volume: Union[int, float, None]
    origin: Optional[str]
    production_year: Optional[int]


class CarEnginesList(ApiModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[CarEngine]


class Customer(ApiModel):
    id: int
    passport_number: int
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    age: Optional[int]
    city: Optional[str]


class CustomerInfo(ApiModel):
    id: int
    passport_number: int
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    age: int
    city: Optional[str]


class CustomerStrict(ApiModel):
    id: int
    passport_number: int
    first_name: str
    last_name: str
    email: str
    age: int
    city: str


class CarsListItem(ApiModel):
    id: int
    car_owner: Customer
    plate_number: str
    brand: Optional[str]
    model: Optional[str]
    engine_number: str


class CarsList(ApiModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[CarsListItem]


class Car(ApiModel):
    id: int
    plate_number: str
    brand: Optional[str]
    model: Optional[str]
    engine_number: Optional[str]
    car_owner: int


class CarInfo(ApiModel):
    id: int
    car_owner: CustomerInfo
    plate_number: str
    brand: Optional[str]
    model: Optional[str]
    engine_number: Optional[str]


class CustomersList(ApiModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[Customer]


class Root(ApiModel):
    cars: str
    car_engines: str
    customers: str
    operations: str
    services: str
    payments: str


class PaymentListItem(ApiModel):
    id: Optional[int]
    amount: Optional[str]
    currency: Optional[str]
    timestamp: Optional[str]
    InvId: Optional[str]
    trsid: Optional[str]
    custom: Optional[str]
    signature: Optional[str]
    status: Optional[str]


class PaymentsList(ApiModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[PaymentListItem]


class Payment(ApiModel):
    id: int
    amount: str
    currency: str
    timestamp: str
    InvId: str
    trsid: str
    custom: str
    signature: Optional[str]
    status: str


class PaymentsSuccess(ApiModel):
    status: str
    message: str


class OperationCar(ApiModel):
    id: int
    car_owner: CustomerStrict
    plate_number: str
    brand: str
    model: str
    engine_number: str


class OperationService(ApiModel):
    id: int
    service_name: str
    service_cost_usd: Union[float, int, None]


class OperationListItem(ApiModel):
    id: int
    car: OperationCar
    service: OperationService
    payment_status: str
    can_be_done: bool
    final_price: str
    operation_status: str
    operation_timestamp: str
    payment: Optional[int]


class OperationsList(ApiModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[OperationListItem]


class Operation(ApiModel):
    id: int
    final_price: str
    operation_status: Optional[str]
    operation_timestamp: str
    car: int
    service: int
    payment: Optional[int]


class OperationDetails(ApiModel):
    id: int
    car: OperationCar
    service: OperationService
    payment_status: str
    can_be_done: bool
    final_price: str
    operation_status: str
    operation_timestamp: str
    payment: Optional[int]


class Service(ApiModel):
    id: int
    service_name: Optional[str]
    service_cost_usd: Union[float, int, None]


class ServicesList(ApiModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[Service]


class DiscountService(RootModel[list[Service]]):
    pass


administration = Administration
user_login = UserLogin
refresh_token = RefreshToken
car_engines_list = CarEnginesList
car_engines = CarEngine
cars_list = CarsList
car = Car
car_info = CarInfo
customers_list = CustomersList
customer = Customer
root = Root
payments_list = PaymentsList
payments = Payment
payments_sucsess = PaymentsSuccess
operations_list = OperationsList
operations = Operation
operation_details = OperationDetails
services_list = ServicesList
service = Service
discont_service = DiscountService
