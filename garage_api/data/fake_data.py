import random
from faker import Faker
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

#
# def generate_random_article():
#     article_data = {
#         "title": fake.text(max_nb_chars=80),
#         "description": fake.paragraph(),
#         "body": fake.paragraph(),
#         "tags": [],
#         "comments": fake.paragraph()
#     }
#     num_tags = random.randint(1, 5)
#     for _ in range(num_tags):
#         article_data["tags"].append(fake.word())
#     return article_data
