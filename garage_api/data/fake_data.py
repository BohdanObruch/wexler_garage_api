import random
from faker import Faker

from garage_api.utils.sessions import garage

fake = Faker()


def generate_random_car_engines():
    engine_number_length = random.randint(10, 17)
    engine_number = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(engine_number_length))
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
        "production_year": int(fake.year())
    }
    return data


def random_car_owner(token):
    headers = {
        'Authorization': 'Bearer ' + token[0]
    }
    response = garage().get('/cars/',
                            headers=headers,
                            )

    unique_ids = set()

    for i in response.json()["results"]:
        unique_ids.add(i["car_owner"]["id"])
    random_id = random.choice(list(unique_ids))
    return random_id


def generate_random_cars(token):
    owner = random_car_owner(token)
    plate_number = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
    brand = fake.company()
    model = fake.street_suffix()
    engine_number_length = random.randint(10, 17)
    engine_number = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(engine_number_length))

    data = {
        "plate_number": plate_number,
        "brand": brand,
        "model": model,
        "engine_number": engine_number,
        "car_owner": owner
    }
    return data


def random_car_id(token):
    headers = {
        'Authorization': 'Bearer ' + token[0]
    }
    response = garage().get('/cars/',
                            headers=headers,
                            )
    list_id = []
    for i in response.json()["results"]:
        list_id.append(i["id"])
    random_id = random.choice(list_id)
    return random_id
