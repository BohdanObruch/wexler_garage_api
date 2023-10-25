import random
from garage_api.utils.sessions import garage


def list_car_engines(token):
    headers = {
        'Authorization': 'Bearer ' + token[0]
    }
    response = garage().get('/car_engines/',
                            headers=headers,
                            )
    list_id = []
    for i in response.json()["results"]:
        list_id.append(i["id"])
    random_id = random.choice(list_id)
    return random_id

