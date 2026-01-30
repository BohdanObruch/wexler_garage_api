from garage_api.utils.sessions import garage
import random


class Customers:
    @staticmethod
    def random_customer_id(token):
        headers = {"Authorization": "Bearer " + token[0]}
        response = garage().get(
            "/customers/",
            headers=headers,
        )
        list_id = []
        for i in response.json()["results"]:
            list_id.append(i["id"])
        random_id = random.choice(list_id)
        return random_id
