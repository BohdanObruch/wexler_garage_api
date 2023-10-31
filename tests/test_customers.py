from pytest import mark
from garage_api.data.fake_data import random_customers
from garage_api.schemas.garage import customers_list, customer
from garage_api.utils.sessions import garage
from pytest_voluptuous import S
from garage_api.helpers import app


class TestCustomers:

    @mark.testomatio('@Tc1dd0300')
    def test_list_customers(self, token):
        response = garage().get(
            '/customers/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(customers_list) == response.json()
        assert response.json()['count'] == len(response.json()['results'])

    @mark.testomatio('@Tac449165')
    def test_create_customers_post(self, token):
        data = random_customers()
        response = garage().post(
            '/customers/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 201
        assert S(customer) == response.json()
        assert response.json()['passport_number'] == data['passport_number']
        assert response.json()['first_name'] == data['first_name']
        assert response.json()['last_name'] == data['last_name']
        assert response.json()['email'] == data['email']
        assert response.json()['age'] == data['age']
        assert response.json()['city'] == data['city']

    @mark.testomatio('@T67e026dd')
    def test_create_customers_put(self, token):
        data = random_customers()
        response = garage().put(
            '/customers/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 201
        assert S(customer) == response.json()
        assert response.json()['passport_number'] == data['passport_number']
        assert response.json()['first_name'] == data['first_name']
        assert response.json()['last_name'] == data['last_name']
        assert response.json()['email'] == data['email']
        assert response.json()['age'] == data['age']
        assert response.json()['city'] == data['city']

    @mark.testomatio('@T72dc66aa')
    def test_details_by_random_customer(self, token):
        random_id = app.customers.random_customer_id(token)
        response = garage().get(
            f'/customers/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(customer) == response.json()
        assert response.json()['id'] == random_id

    @mark.testomatio('@Tc192568f')
    def test_update_customer(self, token):
        data = random_customers()
        random_id = app.customers.random_customer_id(token)
        response = garage().put(
            f'/customers/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(customer) == response.json()
        assert response.json()['passport_number'] == data['passport_number']
        assert response.json()['first_name'] == data['first_name']
        assert response.json()['last_name'] == data['last_name']
        assert response.json()['email'] == data['email']
        assert response.json()['age'] == data['age']
        assert response.json()['city'] == data['city']

    @mark.testomatio('@T2abe1187')
    def test_partial_update_customer(self, token):
        random_data = random_customers()
        passport_number = random_data['passport_number']
        data = {'passport_number': passport_number}
        random_id = app.customers.random_customer_id(token)
        response = garage().patch(
            f'/customers/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(customer) == response.json()
        assert response.json()['passport_number'] == data['passport_number']

    @mark.testomatio('@T3c10d07f')
    def test_delete_customer(self, token):
        random_id = app.customers.random_customer_id(token)
        response = garage().delete(
            f'/customers/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        if response.status_code != 204:
            assert "Cannot delete some instances of model 'Customer' because they are referenced through restricted foreign keys" in response.text
        else:
            assert response.status_code == 204
            assert response.text == ''
