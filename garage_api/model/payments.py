import random
from faker import Faker
# from garage_api.data.fake_data import random_payments
from garage_api.utils.sessions import garage
from garage_api.helpers import app

fake = Faker()


class Payments:

    @staticmethod
    def create_random_payments():
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

    def create_payments(self, token):
        random_data = self.create_random_payments()
        response = garage().post('/payments/',
                                 headers={'Authorization': 'Bearer ' + token[0]},
                                 data=random_data
                                 )
        id = response.json()['id']
        return id

    @staticmethod
    def list_payments(token):
        unique_ids = app.operations.list_of_paid_transactions(token)
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

    @staticmethod
    def random_payments(token):
        response = garage().get('/payments/',
                                headers={'Authorization': 'Bearer ' + token[0]})
        if response.json()['count'] > 0:
            list_id = []
            for i in response.json()["results"]:
                list_id.append(i["id"])
            random_id = random.choice(list_id)
            return random_id
