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


def generate_random_customers():
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
        "city": city
    }
    return data


def random_customer_id(token):
    headers = {
        'Authorization': 'Bearer ' + token[0]
    }
    response = garage().get('/customers/',
                            headers=headers,
                            )
    list_id = []
    for i in response.json()["results"]:
        list_id.append(i["id"])
    random_id = random.choice(list_id)
    return random_id


def generate_random_payments():
    amount = round(random.uniform(10.00, 99.00), 2)
    amount = f"{amount:.2f}"

    currency = random.choice(["USD", "TRY", "EUR", "GBP", "CNY"])
    inv_id = str(random.randint(1, 999))
    trs_id = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    custom = fake.sentence(nb_words=2)
    signature = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
    status = "SUCCESS"

    data = {
        "amount": amount,
        "currency": currency,
        "InvId": inv_id,
        "trsid": trs_id,
        "custom": custom,
        "signature": signature,
        "status": status
    }
    return data


def random_payments_id(token):
    response = garage().get('/payments/',
                            headers={'Authorization': 'Bearer ' + token[0]})
    if response.json()['count'] > 0:
        list_id = []
        for i in response.json()["results"]:
            list_id.append(i["id"])
        random_id = random.choice(list_id)
        return random_id


def generate_random_operations(token):
    car = random_car_id(token)
    service = random_service_id(token)
    payment = random_payments_id(token)
    amount = round(random.uniform(10.00, 99.00), 2)
    operation_status = random.choice(["started", "in progress"])
    price = f"{amount:.2f}"

    data = {
        "final_price": price,
        "operation_status": operation_status,
        "car": car,
        "service": service,
        "payment": payment
    }
    return data


def random_service_id(token):
    response = garage().get('/services/',
                            headers={'Authorization': 'Bearer ' + token[0]})
    if response.json()['count'] > 0:
        list_id = []
        for i in response.json()["results"]:
            if i["service_cost_usd"] is not None:
                list_id.append(i["id"])
        random_id = random.choice(list_id)
        return random_id


def generate_services():
    service_name = fake.sentence(nb_words=2)
    service_cost = round(random.uniform(10.00, 99.00), 2)
    data = {
        "service_name": service_name,
        "service_cost_usd": service_cost
    }
    return data


def generate_discount():
    discount = random.randint(1, 99)
    data = {
        "discount": discount
    }
    return data


def random_operations_id(token):
    response = garage().get('/operations/',
                            headers={'Authorization': 'Bearer ' + token[0]})
    if response.json()['count'] > 0:
        list_id = []
        for i in response.json()["results"]:
            list_id.append(i["id"])
        random_id = random.choice(list_id)
        return random_id


def operations_is_not_finish(token):
    response = garage().get('/operations/',
                            headers={'Authorization': 'Bearer ' + token[0]})
    if response.json()['count'] > 0:
        list_id = []
        for i in response.json()["results"]:
            if i["operation_status"] != "finished":
                list_id.append(i["id"])
        if len(list_id) > 0:
            random_id = random.choice(list_id)
            return random_id


def operations_is_in_progress(token):
    response = garage().get('/operations/',
                            headers={'Authorization': 'Bearer ' + token[0]})
    if response.json()['count'] > 0:
        list_id = []
        for i in response.json()["results"]:
            if i["operation_status"] == "started":
                if i["payment"] is not None:
                    list_id.append(i["id"])
        if len(list_id) > 0:
            random_id = random.choice(list_id)
            return random_id

