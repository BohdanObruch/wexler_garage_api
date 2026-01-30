from __future__ import annotations

from garage_api.schemas.garage import (
    Administration,
    ApiModel,
    Car,
    CarEngine,
    CarEnginesList,
    CarInfo,
    CarsList,
    Customer,
    CustomersList,
    DiscountService,
    Operation,
    OperationDetails,
    OperationsList,
    Payment,
    PaymentsList,
    PaymentsSuccess,
    RefreshToken,
    Root,
    Service,
    ServicesList,
    UserLogin,
)


AdministrationResponseSchema = Administration


CarEngineResponseSchema = CarEngine


CarEnginesListResponseSchema = CarEnginesList


CustomerResponseSchema = Customer


CustomersListResponseSchema = CustomersList


CarResponseSchema = Car


CarInfoResponseSchema = CarInfo


CarsListResponseSchema = CarsList


OperationResponseSchema = Operation


OperationDetailsResponseSchema = OperationDetails


OperationsListResponseSchema = OperationsList


PaymentResponseSchema = Payment


PaymentsListResponseSchema = PaymentsList


PaymentsSuccessResponseSchema = PaymentsSuccess


RootResponseSchema = Root


ServiceResponseSchema = Service


ServicesListResponseSchema = ServicesList


DiscountServiceResponseSchema = DiscountService


UserLoginResponseSchema = UserLogin


RefreshTokenResponseSchema = RefreshToken


class KitchenResponseSchema(ApiModel):
    result: str


__all__ = [
    "AdministrationResponseSchema",
    "CarEngineResponseSchema",
    "CarEnginesListResponseSchema",
    "CustomerResponseSchema",
    "CustomersListResponseSchema",
    "CarResponseSchema",
    "CarInfoResponseSchema",
    "CarsListResponseSchema",
    "OperationResponseSchema",
    "OperationDetailsResponseSchema",
    "OperationsListResponseSchema",
    "PaymentResponseSchema",
    "PaymentsListResponseSchema",
    "PaymentsSuccessResponseSchema",
    "RootResponseSchema",
    "ServiceResponseSchema",
    "ServicesListResponseSchema",
    "DiscountServiceResponseSchema",
    "UserLoginResponseSchema",
    "RefreshTokenResponseSchema",
    "KitchenResponseSchema",
]
