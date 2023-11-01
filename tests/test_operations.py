from garage_api.data.fake_data import random_operations
from garage_api.schemas.garage import operations_list, operations, operation_details
from garage_api.utils.sessions import garage
from pytest_voluptuous import S
from datetime import datetime
from garage_api.helpers import app


class TestOperations:

    def test_operations_list(self, token):
        response = garage().get(
            '/operations/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(operations_list) == response.json()
        assert response.json()['count'] == len(response.json()['results'])

    def test_create_operations(self, token):
        data = random_operations(token)
        response = garage().post(
            '/operations/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        timestamp_format = '%d/%m/%Y %H:%M:%S'
        assert response.status_code == 201
        assert S(operations) == response.json()
        assert response.json()['final_price'] == data['final_price']
        assert response.json()['operation_status'] == data['operation_status']
        assert response.json()['car'] == data['car']
        assert response.json()['service'] == data['service']
        assert response.json()['payment'] == data['payment']
        assert 'id' in response.json()
        assert datetime.strptime(response.json().get(
            'operation_timestamp'), timestamp_format)

    def test_init_operations(self, token):
        random_data = app.operations.random_operations_init(token)
        params = {
            'plate_number': random_data[0], 'service_name': random_data[1]}
        response = garage().get('/operations/init/',
                                headers={'Authorization': 'Bearer ' + token[0]}, params=params)
        assert response.status_code == 200
        assert S(operation_details) == response.json()
        assert response.json()['car']['plate_number'] == params['plate_number']
        assert response.json()[
            'service']['service_name'] == params['service_name']
        assert response.json()['operation_status'] != 'in progress'

    def test_details_by_random_operations(self, token):
        random_id = app.operations.random_operations_id(token)
        response = garage().get(
            f'/operations/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(operation_details) == response.json()
        assert response.json()['id'] == random_id

    def test_update_operations(self, token):
        data = random_operations(token)
        random_id = app.operations.random_operations_id(token)
        response = garage().put(
            f'/operations/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        timestamp_format = '%d/%m/%Y %H:%M:%S'
        assert response.status_code == 200
        assert S(operations) == response.json()
        assert response.json()['final_price'] == data['final_price']
        assert response.json()['operation_status'] == data['operation_status']
        assert response.json()['car'] == data['car']
        assert response.json()['service'] == data['service']
        assert response.json()['payment'] == data['payment']
        assert 'id' in response.json()
        assert datetime.strptime(response.json().get(
            'operation_timestamp'), timestamp_format)

    def test_partial_update_operations(self, token):
        random_data = random_operations(token)
        data = {'final_price': random_data['final_price'],
                'operation_status': random_data['operation_status']}
        random_id = app.operations.random_operations_id(token)
        response = garage().patch(
            f'/operations/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(operations) == response.json()
        assert response.json()['final_price'] == data['final_price']
        assert response.json()['operation_status'] == data['operation_status']

    def test_delete_operations(self, token):
        random_id = app.operations.random_operations_id(token)
        response = garage().delete(
            f'/operations/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 204
        assert response.text == ''

    def test_finished_operations(self, token):
        random_id = app.operations.operations_is_not_finish(token)
        if random_id is not None:
            response = garage().get(
                f'/operations/{random_id}/finished/', headers={'Authorization': 'Bearer ' + token[0]})
            assert response.status_code == 200
            assert S(operation_details) == response.json()
            assert response.json()['operation_status'] == 'finished'
            assert response.json()['id'] == random_id

    def test_operations_in_progress(self, token):
        random_id = app.operations.operations_is_in_progress(token)
        response = garage().get(
            f'/operations/{random_id}/in_progress/', headers={'Authorization': 'Bearer ' + token[0]})
        if response.status_code == 200:
            assert S(operation_details) == response.json()
            assert response.json()['operation_status'] == 'in progress'
            assert response.json()['id'] == random_id

    def test_stop_operations(self, token):
        random_id = app.operations.random_operations_id(token)
        response = garage().get(
            f'/operations/{random_id}/stop/', headers={'Authorization': 'Bearer ' + token[0]})
        if response.status_code == 200:
            assert S(operation_details) == response.json()
            assert response.json()['operation_status'] == 'stopped'
            assert response.json()['id'] == random_id
