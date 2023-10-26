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
