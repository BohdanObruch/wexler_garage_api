from garage_api.schemas.garage import payments_list, payments, payments_sucsess
from garage_api.utils.sessions import garage
from pytest_voluptuous import S
from datetime import datetime
from garage_api.helpers import app


class TestPayments:
    def test_payments_list(self, token):
        response = garage().get('/payments/',
                                headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(payments_list) == response.json()
        assert response.json()['count'] == len(response.json()['results'])

    def test_create_payments_post(self, token):
        data = app.payments.create_random_payments()
        response = garage().post('/payments/',
                                 headers={'Authorization': 'Bearer ' + token[0]},
                                 data=data
                                 )
        timestamp_format = "%d/%m/%Y %H:%M:%S"
        assert response.status_code == 201
        assert S(payments) == response.json()
        assert response.json()['amount'] == data['amount']
        assert response.json()['currency'] == data['currency']
        assert response.json()['InvId'] == data['InvId']
        assert response.json()['trsid'] == data['trsid']
        assert response.json()['custom'] == data['custom']
        assert response.json()['signature'] == data['signature']
        assert response.json()['status'] == data['status']
        assert 'id' in response.json()
        assert datetime.strptime(response.json().get('timestamp'), timestamp_format)

    def test_create_payments_put(self, token):
        data = app.payments.create_random_payments()
        response = garage().put('/payments/',
                                headers={'Authorization': 'Bearer ' + token[0]},
                                data=data
                                )
        timestamp_format = "%d/%m/%Y %H:%M:%S"
        assert response.status_code == 201
        assert S(payments) == response.json()
        assert response.json()['amount'] == data['amount']
        assert response.json()['currency'] == data['currency']
        assert response.json()['InvId'] == data['InvId']
        assert response.json()['trsid'] == data['trsid']
        assert response.json()['custom'] == data['custom']
        assert response.json()['signature'] == data['signature']
        assert response.json()['status'] == data['status']
        assert 'id' in response.json()
        assert datetime.strptime(response.json().get('timestamp'), timestamp_format)

    def test_payments_success(self, token):
        inv_id = app.payments.list_payments(token)
        random_data = app.payments.create_random_payments()
        data = {
            "amount": random_data['amount'],
            "currency": random_data['currency'],
            "InvId": inv_id,
            "trsid": random_data['trsid'],
            "custom": random_data['custom'],
            "signature": random_data['signature'],
            "status": "SUCCESS"
        }
        if inv_id is not None:
            response = garage().post('/payments/success/',
                                     headers={'Authorization': 'Bearer ' + token[0]},
                                     data=data)
            assert response.status_code == 200
            assert S(payments_sucsess) == response.json()
            assert response.json()['status'] == 'SUCCESS'

    def test_read_payments(self, token):
        id = app.payments.random_payments(token)
        response = garage().get(f'/payments/{id}/',
                                headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(payments) == response.json()
        assert response.json()['id'] == id

    def test_update_payments(self, token):
        random_data = app.payments.create_random_payments()
        data = {
            "amount": random_data['amount'],
            "currency": random_data['currency'],
            "InvId": random_data['InvId'],
            "trsid": random_data['trsid'],
            "custom": random_data['custom'],
            "signature": random_data['signature'],
            "status": "SUCCESS"
        }
        id = app.payments.random_payments(token)
        response = garage().put(f'/payments/{id}/',
                                headers={'Authorization': 'Bearer ' + token[0]},
                                data=data
                                )
        assert response.status_code == 200
        assert S(payments) == response.json()
        assert response.json()['status'] == data['status']

    def test_partial_update_payments(self, token):
        data = {
            "status": "SUCCESS"
        }

        id = app.payments.random_payments(token)
        response = garage().patch(f'/payments/{id}/',
                                  headers={'Authorization': 'Bearer ' + token[0]},
                                  data=data
                                  )
        assert response.status_code == 200
        assert S(payments) == response.json()
        assert response.json()['status'] == data['status']

    def test_delete_payments(self, token):
        id = app.payments.random_payments(token)
        response = garage().delete(f'/payments/{id}/',
                                   headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 204
        assert response.text == ''
