from garage_api.utils.sessions import garage
import random


class Cars:
    @staticmethod
    def random_car_owner(token):
        headers = {"Authorization": "Bearer " + token[0]}
        response = garage().get(
            "/cars/",
            headers=headers,
        )

        unique_ids = set()

        for i in response.json()["results"]:
            unique_ids.add(i["car_owner"]["id"])
        random_id = random.choice(list(unique_ids))
        return random_id

    @staticmethod
    def random_car_id(token):
        headers = {"Authorization": "Bearer " + token[0]}
        response = garage().get(
            "/cars/",
            headers=headers,
        )
        list_id = []
        for i in response.json()["results"]:
            list_id.append(i["id"])
        random_id = random.choice(list_id)
        return random_id
