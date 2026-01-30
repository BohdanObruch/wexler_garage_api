from garage_api.utils.sessions import garage
import random


class Operations:
    @staticmethod
    def random_operations_id(token):
        response = garage().get(
            "/operations/", headers={"Authorization": "Bearer " + token[0]}
        )
        if response.json()["count"] > 0:
            list_id = []
            for i in response.json()["results"]:
                list_id.append(i["id"])
            random_id = random.choice(list_id)
            return random_id

    @staticmethod
    def operations_is_not_finish(token):
        response = garage().get(
            "/operations/", headers={"Authorization": "Bearer " + token[0]}
        )
        if response.json()["count"] > 0:
            list_id = []
            for i in response.json()["results"]:
                if i["operation_status"] != "finished":
                    list_id.append(i["id"])
            if len(list_id) > 0:
                random_id = random.choice(list_id)
                return random_id

    @staticmethod
    def operations_is_in_progress(token):
        response = garage().get(
            "/operations/", headers={"Authorization": "Bearer " + token[0]}
        )
        if response.json()["count"] > 0:
            list_id = []
            for i in response.json()["results"]:
                if i["operation_status"] == "started":
                    if i["payment"] is not None:
                        if i["payment_status"] == "Оплачено":
                            list_id.append(i["id"])
            if len(list_id) > 0:
                random_id = random.choice(list_id)
                return random_id

    @staticmethod
    def random_operations_init(token):
        response = garage().get(
            "/operations/", headers={"Authorization": "Bearer " + token[0]}
        )
        if response.json()["count"] > 0:
            results = response.json()["results"]
            result_pairs = []
            for result in results:
                if result["operation_status"] == "started":
                    engine_number = result["car"]["plate_number"]
                    service_name = result["service"]["service_name"]
                    result_pairs.append((engine_number, service_name))
            random_data = random.choice(result_pairs)
            return random_data

    @staticmethod
    def list_of_paid_transactions(token):
        response = garage().get(
            "/operations/", headers={"Authorization": "Bearer " + token[0]}
        )
        if response.json()["count"] > 0:
            list_payment_id = set()
            for i in response.json()["results"]:
                if i["payment"] is not None:
                    list_payment_id.add(i["payment"])

            unique_ids = list(list_payment_id)
            if len(unique_ids) > 0:
                return unique_ids
