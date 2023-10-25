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
