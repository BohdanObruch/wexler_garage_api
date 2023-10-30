from voluptuous import Schema, Any

administration = Schema({
    "status": str,
    "message": str
})

user_login = Schema({
    "refresh": str,
    "access": str
})

refresh_token = Schema({
    "access": str
})

car_engines_list = Schema({
    "count": int,
    "next": Any(str, None),
    "previous": Any(str, None),
    "results": [
        {
            "id": int,
            "engine_number": str,
            "volume": Any(int, float, None),
            "origin": Any(str, None),
            "production_year": Any(int, None),
        }
    ]
})

car_engines = Schema({
    "id": int,
    "engine_number": str,
    "volume": Any(int, float, None),
    "origin": Any(str, None),
    "production_year": Any(int, None),
})

cars_list = Schema({
    "count": int,
    "next": Any(str, None),
    "previous": Any(str, None),
    "results": [
        {
            "id": int,
            "car_owner": {
                "id": int,
                "passport_number": int,
                "first_name": Any(str, None),
                "last_name": Any(str, None),
                "email": Any(str, None),
                "age": Any(int, None),
                "city": Any(str, None)
            },
            "plate_number": str,
            "brand": Any(str, None),
            "model": Any(str, None),
            "engine_number": str
        }
    ]
})

car = Schema({
    "id": int,
    "plate_number": str,
    "brand": Any(str, None),
    "model": Any(str, None),
    "engine_number": Any(str, None),
    "car_owner": int
})

car_info = Schema({
    "id": int,
    "car_owner": {
        "id": int,
        "passport_number": int,
        "first_name": Any(str, None),
        "last_name": Any(str, None),
        "email": Any(str, None),
        "age": int,
        "city": Any(str, None)
    },
    "plate_number": str,
    "brand": Any(str, None),
    "model": Any(str, None),
    "engine_number": Any(str, None)
})

customers_list = Schema({
    "count": int,
    "next": Any(str, None),
    "previous": Any(str, None),
    "results": [
        {
            "id": int,
            "passport_number": int,
            "first_name": Any(str, None),
            "last_name": Any(str, None),
            "email": Any(str, None),
            "age": Any(int, None),
            "city": Any(str, None)
        }
    ]
})

customer = Schema({
    "id": int,
    "passport_number": int,
    "first_name": Any(str, None),
    "last_name": Any(str, None),
    "email": Any(str, None),
    "age": Any(int, None),
    "city": Any(str, None)
})

root = Schema({
    "cars": str,
    "car_engines": str,
    "customers": str,
    "operations": str,
    "services": str,
    "payments": str
})

payments_list = Schema({
    "count": int,
    "next": Any(str, None),
    "previous": Any(str, None),
    "results": [
        {
            "id": Any(int, None),
            "amount": Any(str, None),
            "currency": Any(str, None),
            "timestamp": Any(str, None),
            "InvId": Any(str, None),
            "trsid": Any(str, None),
            "custom": Any(str, None),
            "signature": Any(str, None),
            "status": Any(str, None)
        }
    ]
})

payments = Schema({
    "id": int,
    "amount": str,
    "currency": str,
    "timestamp": str,
    "InvId": str,
    "trsid": str,
    "custom": str,
    "signature": Any(str, None),
    "status": str
})

payments_sucsess = Schema({
    "status": str,
    "message": str
})

operations_list = Schema({
    "count": int,
    "next": Any(str, None),
    "previous": Any(str, None),
    "results": [
        {
            "id": int,
            "car": {
                "id": int,
                "car_owner": {
                    "id": int,
                    "passport_number": int,
                    "first_name": str,
                    "last_name": str,
                    "email": str,
                    "age": int,
                    "city": str
                },
                "plate_number": str,
                "brand": str,
                "model": str,
                "engine_number": str
            },
            "service": {
                "id": int,
                "service_name": str,
                "service_cost_usd": Any(float, int, None),
            },
            "payment_status": str,
            "can_be_done": bool,
            "final_price": str,
            "operation_status": str,
            "operation_timestamp": str,
            "payment": Any(int, None)
        },
    ]
})

operations = Schema({
    "id": int,
    "final_price": str,
    "operation_status": Any(str, None),
    "operation_timestamp": str,
    "car": int,
    "service": int,
    "payment": Any(int, None)
})

operation_details = Schema({
    "id": int,
    "car": {
        "id": int,
        "car_owner": {
            "id": int,
            "passport_number": int,
            "first_name": str,
            "last_name": str,
            "email": str,
            "age": int,
            "city": str
        },
        "plate_number": str,
        "brand": str,
        "model": str,
        "engine_number": str
    },
    "service": {
        "id": int,
        "service_name": str,
        "service_cost_usd": Any(float, None),
    },
    "payment_status": str,
    "can_be_done": bool,
    "final_price": str,
    "operation_status": str,
    "operation_timestamp": str,
    "payment": Any(int, None)
})

services_list = Schema({
    "count": int,
    "next": Any(str, None),
    "previous": Any(str, None),
    "results": [
        {
            "id": int,
            "service_name": str,
            "service_cost_usd": Any(float, int, None),
        }
    ]
})

service = Schema({
    "id": int,
    "service_name": Any(str, None),
    "service_cost_usd": Any(float, None),
})

discont_service = Schema([
        {
            "id": int,
            "service_name": Any(str, None),
            "service_cost_usd": Any(float, None),
        }
    ])
