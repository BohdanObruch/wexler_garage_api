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
    inv_id = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    trs_id = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    custom = fake.sentence(nb_words=2)
    signature = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
    status = random.choice(["SUCCESS", "IN PROGRESS", "FAILED"])
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


def create_payments(token):
    random_data = generate_random_payments()
    response = garage().post('/payments/',
                             headers={'Authorization': 'Bearer ' + token[0]},
                             data=random_data
                             )
    id = response.json()['id']
    return id


def list_payments(token):
    unique_ids = list_of_paid_transactions(token)
    response = garage().get('/payments/',
                            headers={'Authorization': 'Bearer ' + token[0]})
    list_inv_id = []
    for i in response.json()["results"]:
        if i["status"] != "SUCCESS":
            if i["id"] in unique_ids:
                list_inv_id.append(i["InvId"])
    if len(list_inv_id) > 0:
        inv_id = random.choice(list_inv_id)
        return inv_id


def random_payments(token):
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
    id_payment = create_payments(token)
    amount = round(random.uniform(10.00, 99.00), 2)
    price = f"{amount:.2f}"

    data = {
        "final_price": price,
        "operation_status": "started",
        "car": car,
        "service": service,
        "payment": id_payment
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
                    if i["payment_status"] == "Оплачено":
                        list_id.append(i["id"])
        if len(list_id) > 0:
            random_id = random.choice(list_id)
            return random_id


def random_operations_init(token):
    response = garage().get('/operations/',
                            headers={'Authorization': 'Bearer ' + token[0]})
    if response.json()['count'] > 0:
        results = response.json()["results"]
        result_pairs = []
        for result in results:
            if result["operation_status"] == "started":
                engine_number = result["car"]["plate_number"]
                service_name = result["service"]["service_name"]
                result_pairs.append((engine_number, service_name))
        random_data = random.choice(result_pairs)
        return random_data


def list_of_paid_transactions(token):
    response = garage().get('/operations/',
                            headers={'Authorization': 'Bearer ' + token[0]})
    if response.json()['count'] > 0:
        list_payment_id = set()
        for i in response.json()["results"]:
            if i["payment"] is not None:
                list_payment_id.add(i["payment"])

        unique_ids = list(list_payment_id)
        if len(unique_ids) > 0:
            return unique_ids
