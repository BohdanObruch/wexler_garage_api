from garage_api.utils.sessions import garage
import random


class Services:
    @staticmethod
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
