from pytest import mark
from garage_api.data.fake_data import random_car_engines
from garage_api.utils.sessions import garage
from pytest_voluptuous import S
from garage_api.schemas.garage import car_engines_list, car_engines
from garage_api.helpers import app


class TestCarEngines:

    @mark.testomatio('@Taf3227a5')
    def test_list_car_engines(self, token):
        headers = {'Authorization': 'Bearer ' + token[0]}
        response = garage().get('/car_engines/', headers=headers)
        assert response.status_code == 200
        assert S(car_engines_list) == response.json()
        assert response.json()['count'] == len(response.json()['results'])

    @mark.testomatio('@Tf6efb6bc')
    def test_create_car_engines_post(self, token):
        data = random_car_engines()
        response = garage().post(
            '/car_engines/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 201
        assert S(car_engines) == response.json()
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['volume'] == data['volume']
        assert response.json()['origin'] == data['origin']
        assert response.json()['production_year'] == data['production_year']

    @mark.testomatio('@Ta51b9ee5')
    def test_create_car_engines_put(self, token):
        data = random_car_engines()
        response = garage().put(
            '/car_engines/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 201
        assert S(car_engines) == response.json()
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['volume'] == data['volume']
        assert response.json()['origin'] == data['origin']
        assert response.json()['production_year'] == data['production_year']

    @mark.testomatio('@T5aa4108f')
    def test_details_by_random_engine_number(self, token):
        random_id = app.car_enines.random_car_engines_id(token)
        response = garage().get(
            f'/car_engines/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(car_engines) == response.json()
        assert response.json()['id'] == random_id

    @mark.testomatio('@T3e198455')
    def test_update_car_engines(self, token):
        data = random_car_engines()
        random_id = app.car_enines.random_car_engines_id(token)
        response = garage().put(
            f'/car_engines/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(car_engines) == response.json()
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['volume'] == data['volume']
        assert response.json()['origin'] == data['origin']
        assert response.json()['production_year'] == data['production_year']

    @mark.testomatio('@Te7f40504')
    def test_partial_update_car_engines(self, token):
        random_data = random_car_engines()
        engine_number = random_data['engine_number']
        volume = random_data['volume']
        random_id = app.car_enines.random_car_engines_id(token)
        data = {'engine_number': engine_number, 'volume': volume}
        response = garage().patch(
            f'/car_engines/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(car_engines) == response.json()
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['volume'] == data['volume']

    @mark.testomatio('@Td2ad26d0')
    def test_delete_car_engines(self, token):
        random_id = app.car_enines.random_car_engines_id(token)
        response = garage().delete(
            f'/car_engines/{random_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 204
        assert response.text == ''
