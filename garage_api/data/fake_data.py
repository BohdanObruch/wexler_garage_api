import random
from faker import Faker
from garage_api.helpers import app

fake = Faker()


def random_cars(token):
    owner = app.cars.random_car_owner(token)
    plate_number = "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(8)
    )
    brand = fake.company()
    model = fake.street_suffix()
    engine_number_length = random.randint(10, 17)
    engine_number = "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        for _ in range(engine_number_length)
    )

    data = {
        "plate_number": plate_number,
        "brand": brand,
        "model": model,
        "engine_number": engine_number,
        "car_owner": owner,
    }
    return data


def random_customers():
    passport_number = random.randint(10000000, 99999999)
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    age = random.randint(18, 100)
    city = fake.city()

    data = {
        "passport_number": passport_number,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "city": city,
    }
    return data


def random_services():
    service_name = fake.sentence(nb_words=2)
    service_cost = round(random.uniform(10.00, 99.00), 2)
    data = {"service_name": service_name, "service_cost_usd": service_cost}
    return data


def random_discount():
    discount = random.randint(1, 99)
    data = {"discount": discount}
    return data


def random_operations(token):
    car = app.cars.random_car_id(token)
    service = app.services.random_service_id(token)
    id_payment = app.payments.create_payments(token)
    amount = round(random.uniform(10.00, 99.00), 2)
    price = f"{amount:.2f}"

    data = {
        "final_price": price,
        "operation_status": "started",
        "car": car,
        "service": service,
        "payment": id_payment,
    }
    return data


def random_car_engines():
    engine_number_length = random.randint(10, 17)
    engine_number = "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        for _ in range(engine_number_length)
    )
    volume = round(random.uniform(1.0, 9.0), 1)

    origin = None
    while origin is None:
        country = fake.country()
        if len(country) <= 30:
            origin = country

    data = {
        "engine_number": engine_number,
        "volume": volume,
        "origin": origin,
        "production_year": int(fake.year()),
    }
    return data
