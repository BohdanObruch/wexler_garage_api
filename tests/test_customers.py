from garage_api.data.fake_data import generate_random_customers, random_customer_id
from garage_api.schemas.garage import customers_list, customer
from garage_api.utils.sessions import garage
from pytest_voluptuous import S


class TestCustomers:
    def test_list_customers(self, token):
        response = garage().get('/customers/',
                                headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(customers_list) == response.json()
        assert response.json()['count'] == len(response.json()['results'])

    def test_create_customers_post(self, token):
        data = generate_random_customers()
        response = garage().post('/customers/',
                                 headers={'Authorization': 'Bearer ' + token[0]},
                                 data=data
                                 )
        assert response.status_code == 201
        assert S(customer) == response.json()
        assert response.json()['passport_number'] == data['passport_number']
        assert response.json()['first_name'] == data['first_name']
        assert response.json()['last_name'] == data['last_name']
        assert response.json()['email'] == data['email']
        assert response.json()['age'] == data['age']
        assert response.json()['city'] == data['city']

    def test_create_customers_put(self, token):
        data = generate_random_customers()
        response = garage().put('/customers/',
                                headers={'Authorization': 'Bearer ' + token[0]},
                                data=data
                                )
        assert response.status_code == 201
        assert S(customer) == response.json()
        assert response.json()['passport_number'] == data['passport_number']
        assert response.json()['first_name'] == data['first_name']
        assert response.json()['last_name'] == data['last_name']
        assert response.json()['email'] == data['email']
        assert response.json()['age'] == data['age']
        assert response.json()['city'] == data['city']

    def test_details_by_random_customer(self, token):
        random_id = random_customer_id(token)
        response = garage().get(f'/customers/{random_id}/',
                                headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(customer) == response.json()
        assert response.json()['id'] == random_id

    def test_update_customer(self, token):
        data = generate_random_customers()
        random_id = random_customer_id(token)
        response = garage().put(f'/customers/{random_id}/',
                                headers={'Authorization': 'Bearer ' + token[0]},
                                data=data
                                )
        assert response.status_code == 200
        assert S(customer) == response.json()
        assert response.json()['passport_number'] == data['passport_number']
        assert response.json()['first_name'] == data['first_name']
        assert response.json()['last_name'] == data['last_name']
        assert response.json()['email'] == data['email']
        assert response.json()['age'] == data['age']
        assert response.json()['city'] == data['city']

    def test_partial_update_customer(self, token):
        random_data = generate_random_customers()
        passport_number = random_data['passport_number']
        data = {
            "passport_number": passport_number
        }
        random_id = random_customer_id(token)

        response = garage().patch(f'/customers/{random_id}/',
                                  headers={'Authorization': 'Bearer ' + token[0]},
                                  data=data
                                  )
        assert response.status_code == 200
        assert S(customer) == response.json()
        assert response.json()['passport_number'] == data['passport_number']

    def test_delete_customer(self, token):
        random_id = random_customer_id(token)
        print(random_id)
        response = garage().delete(f'/customers/{random_id}/',
                                   headers={'Authorization': 'Bearer ' + token[0]})

        if response.status_code != 204:
            assert ("Cannot delete some instances of model 'Customer' because they are referenced through restricted "
                    "foreign keys") in response.text
            print(response.text)
        else:
            assert response.status_code == 204
            assert response.text == ''
