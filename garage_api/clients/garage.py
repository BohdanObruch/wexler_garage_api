from __future__ import annotations

from typing import Any

from garage_api.clients.base import BaseClient


class AdministrationClient(BaseClient):
    def create_dataset_api(self) -> Any:
        return self._request("GET", "/administration/create_dataset")


class CarsClient(BaseClient):
    def list_cars_api(self, params: dict[str, Any] | None = None) -> Any:
        return self._request("GET", "/cars/", params=params)

    def create_car_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/cars/", data=request.model_dump(exclude_none=True)
        )

    def create_car_put_api(self, request: Any) -> Any:
        return self._request(
            "PUT", "/cars/put/", data=request.model_dump(exclude_none=True)
        )

    def get_car_api(self, car_id: int) -> Any:
        return self._request("GET", f"/cars/{car_id}/")

    def update_car_api(self, car_id: int, request: Any) -> Any:
        return self._request(
            "PUT", f"/cars/{car_id}/", data=request.model_dump(exclude_none=True)
        )

    def partial_update_car_api(self, car_id: int, request: Any) -> Any:
        return self._request(
            "PATCH", f"/cars/{car_id}/", data=request.model_dump(exclude_none=True)
        )

    def delete_car_api(self, car_id: int) -> Any:
        return self._request("DELETE", f"/cars/{car_id}/")


class CarEnginesClient(BaseClient):
    def list_car_engines_api(self, params: dict[str, Any] | None = None) -> Any:
        return self._request("GET", "/car_engines/", params=params)

    def create_car_engine_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/car_engines/", data=request.model_dump(exclude_none=True)
        )

    def create_car_engine_put_api(self, request: Any) -> Any:
        return self._request(
            "PUT", "/car_engines/", data=request.model_dump(exclude_none=True)
        )

    def get_car_engine_api(self, engine_id: int) -> Any:
        return self._request("GET", f"/car_engines/{engine_id}/")

    def update_car_engine_api(self, engine_id: int, request: Any) -> Any:
        return self._request(
            "PUT",
            f"/car_engines/{engine_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def partial_update_car_engine_api(self, engine_id: int, request: Any) -> Any:
        return self._request(
            "PATCH",
            f"/car_engines/{engine_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def delete_car_engine_api(self, engine_id: int) -> Any:
        return self._request("DELETE", f"/car_engines/{engine_id}/")


class CustomersClient(BaseClient):
    def list_customers_api(self, params: dict[str, Any] | None = None) -> Any:
        return self._request("GET", "/customers/", params=params)

    def create_customer_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/customers/", data=request.model_dump(exclude_none=True)
        )

    def create_customer_put_api(self, request: Any) -> Any:
        return self._request(
            "PUT", "/customers/", data=request.model_dump(exclude_none=True)
        )

    def get_customer_api(self, customer_id: int) -> Any:
        return self._request("GET", f"/customers/{customer_id}/")

    def update_customer_api(self, customer_id: int, request: Any) -> Any:
        return self._request(
            "PUT",
            f"/customers/{customer_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def partial_update_customer_api(self, customer_id: int, request: Any) -> Any:
        return self._request(
            "PATCH",
            f"/customers/{customer_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def delete_customer_api(self, customer_id: int) -> Any:
        return self._request("DELETE", f"/customers/{customer_id}/")


class KitchenClient(BaseClient):
    def brew_coffee_api(self) -> Any:
        return self._request("GET", "/kitchen/brew_coffee_in_coffee_maker")


class OperationsClient(BaseClient):
    def list_operations_api(self, params: dict[str, Any] | None = None) -> Any:
        return self._request("GET", "/operations/", params=params)

    def create_operation_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/operations/", data=request.model_dump(exclude_none=True)
        )

    def init_operation_api(self, request: Any) -> Any:
        return self._request(
            "GET", "/operations/init/", params=request.model_dump(exclude_none=True)
        )

    def get_operation_api(self, operation_id: int) -> Any:
        return self._request("GET", f"/operations/{operation_id}/")

    def update_operation_api(self, operation_id: int, request: Any) -> Any:
        return self._request(
            "PUT",
            f"/operations/{operation_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def partial_update_operation_api(self, operation_id: int, request: Any) -> Any:
        return self._request(
            "PATCH",
            f"/operations/{operation_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def delete_operation_api(self, operation_id: int) -> Any:
        return self._request("DELETE", f"/operations/{operation_id}/")

    def finish_operation_api(self, operation_id: int) -> Any:
        return self._request("GET", f"/operations/{operation_id}/finished/")

    def mark_in_progress_api(self, operation_id: int) -> Any:
        return self._request("GET", f"/operations/{operation_id}/in_progress/")

    def stop_operation_api(self, operation_id: int) -> Any:
        return self._request("GET", f"/operations/{operation_id}/stop/")


class PaymentsClient(BaseClient):
    def list_payments_api(self, params: dict[str, Any] | None = None) -> Any:
        return self._request("GET", "/payments/", params=params)

    def create_payment_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/payments/", data=request.model_dump(exclude_none=True)
        )

    def create_payment_put_api(self, request: Any) -> Any:
        return self._request(
            "PUT", "/payments/", data=request.model_dump(exclude_none=True)
        )

    def success_payment_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/payments/success/", data=request.model_dump(exclude_none=True)
        )

    def get_payment_api(self, payment_id: int) -> Any:
        return self._request("GET", f"/payments/{payment_id}/")

    def update_payment_api(self, payment_id: int, request: Any) -> Any:
        return self._request(
            "PUT",
            f"/payments/{payment_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def partial_update_payment_api(self, payment_id: int, request: Any) -> Any:
        return self._request(
            "PATCH",
            f"/payments/{payment_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def delete_payment_api(self, payment_id: int) -> Any:
        return self._request("DELETE", f"/payments/{payment_id}/")


class RootClient(BaseClient):
    def root_api(self) -> Any:
        return self._request("GET", "/root/")


class ServicesClient(BaseClient):
    def list_services_api(self, params: dict[str, Any] | None = None) -> Any:
        return self._request("GET", "/services/", params=params)

    def create_service_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/services/", data=request.model_dump(exclude_none=True)
        )

    def create_service_put_api(self, request: Any) -> Any:
        return self._request(
            "PUT", "/services/", data=request.model_dump(exclude_none=True)
        )

    def get_service_api(self, service_id: int) -> Any:
        return self._request("GET", f"/services/{service_id}/")

    def update_service_api(self, service_id: int, request: Any) -> Any:
        return self._request(
            "PUT",
            f"/services/{service_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def partial_update_service_api(self, service_id: int, request: Any) -> Any:
        return self._request(
            "PATCH",
            f"/services/{service_id}/",
            data=request.model_dump(exclude_none=True),
        )

    def delete_service_api(self, service_id: int) -> Any:
        return self._request("DELETE", f"/services/{service_id}/")

    def apply_discount_api(self, service_id: int, request: Any) -> Any:
        return self._request(
            "GET",
            f"/services/{service_id}/apply_discount/",
            params=request.model_dump(exclude_none=True),
        )

    def apply_discount_v2_api(self, service_id: int, request: Any) -> Any:
        return self._request(
            "GET",
            f"/services/{service_id}/apply_discount_v2/",
            params=request.model_dump(exclude_none=True),
        )

    def apply_discounts_api(self, request: Any) -> Any:
        return self._request(
            "GET",
            "/services/apply_discounts/",
            params=request.model_dump(exclude_none=True),
        )


class AuthClient(BaseClient):
    def __init__(self) -> None:
        super().__init__(auth=True)

    def login_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/user/login/", data=request.model_dump(exclude_none=True)
        )

    def refresh_token_api(self, request: Any) -> Any:
        return self._request(
            "POST", "/user/login/refresh/", data=request.model_dump(exclude_none=True)
        )
