from garage_api.data.fake_data import random_services, random_discount
from garage_api.schemas.garage import services_list, service, discont_service
from garage_api.utils.sessions import garage
from pytest_voluptuous import S
from garage_api.helpers import app


class TestServices:

    def test_services_list(self, token):
        response = garage().get(
            '/services/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(services_list) == response.json()
        assert response.json()['count'] == len(response.json()['results'])

    def test_create_services_post(self, token):
        data = random_services()
        response = garage().post(
            '/services/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 201
        assert S(service) == response.json()
        assert response.json()['service_name'] == data['service_name']
        assert response.json()['service_cost_usd'] == data['service_cost_usd']
        assert 'id' in response.json()

    def test_apply_discounts_v2_services(self, token):
        id = app.services.random_service_id(token)
        discount = random_discount()
        response = garage().get(f'/services/{id}/apply_discount_v2/', headers={
            'Authorization': 'Bearer ' + token[0]}, params=discount)
        assert response.status_code == 200
        assert S(discont_service) == response.json()
        assert response.json()[0]['id'] == id

    def test_create_services_put(self, token):
        data = random_services()
        response = garage().put(
            '/services/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 201
        assert S(service) == response.json()
        assert response.json()['service_name'] == data['service_name']
        assert response.json()['service_cost_usd'] == data['service_cost_usd']
        assert 'id' in response.json()

    def test_details_by_random_service_id(self, token):
        random_id = app.services.random_service_id(token)
        response = garage().get(
            f'/services/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(service) == response.json()
        assert response.json()['id'] == random_id

    def test_update_services(self, token):
        data = random_services()
        random_id = app.services.random_service_id(token)
        response = garage().put(
            f'/services/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(service) == response.json()
        assert response.json()['service_name'] == data['service_name']
        assert response.json()['service_cost_usd'] == data['service_cost_usd']
        assert response.json()['id'] == random_id

    def test_partial_update_services(self, token):
        random_data = random_services()
        service_cost_usd = random_data['service_cost_usd']
        random_id = app.services.random_service_id(token)
        data = {'service_cost_usd': service_cost_usd}
        response = garage().patch(
            f'/services/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(service) == response.json()
        assert response.json()['service_cost_usd'] == data['service_cost_usd']
        assert response.json()['id'] == random_id

    def test_delete_services(self, token):
        random_id = app.services.random_service_id(token)
        response = garage().delete(
            f'/services/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 204
        assert response.text == ''

    def test_apply_discounts_services(self, token):
        id = app.services.random_service_id(token)
        discount = random_discount()
        response = garage().get(f'/services/{id}/apply_discount/', headers={
            'Authorization': 'Bearer ' + token[0]}, params=discount)
        assert response.status_code == 200
        assert S(discont_service) == response.json()
        assert response.json()[0]['id'] == id

    def test_apply_discounts_for_all_services(self, token):
        discount = random_discount()
        response = garage().get(f'/services/apply_discounts/',
                                headers={'Authorization': 'Bearer ' + token[0]}, params=discount)
        assert response.status_code == 200
        assert S(discont_service) == response.json()
