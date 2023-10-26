from garage_api.data.fake_data import generate_random_car_engines
from garage_api.utils.sessions import garage
from pytest_voluptuous import S
from garage_api.schemas.garage import car_engines_list, car_engines
from garage_api.model.car_engines import random_car_engines_id


class TestCarEngines:
    def test_list_car_engines(self, token):
        headers = {
            'Authorization': 'Bearer ' + token[0]
        }
        response = garage().get('/car_engines/',
                                headers=headers,
                                )
        assert response.status_code == 200
        assert S(car_engines_list) == response.json()
        assert response.json()['count'] == len(response.json()['results'])

    def test_create_car_engines_post(self, token):
        data = generate_random_car_engines()

        response = garage().post('/car_engines/',
                                 headers={'Authorization': 'Bearer ' + token[0]},
                                 data=data
                                 )

        assert response.status_code == 201
        assert S(car_engines) == response.json()
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['volume'] == data['volume']
        assert response.json()['origin'] == data['origin']
        assert response.json()['production_year'] == data['production_year']

    def test_create_car_engines_put(self, token):
        data = generate_random_car_engines()
        response = garage().put('/car_engines/',
                                headers={'Authorization': 'Bearer ' + token[0]},
                                data=data
                                )
        assert response.status_code == 201
        assert S(car_engines) == response.json()
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['volume'] == data['volume']
        assert response.json()['origin'] == data['origin']
        assert response.json()['production_year'] == data['production_year']

    def test_details_by_random_engine_number(self, token):
        random_id = random_car_engines_id(token)
        response = garage().get(f'/car_engines/{random_id}/',
                                headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(car_engines) == response.json()
        assert response.json()['id'] == random_id

    def test_update_car_engines(self, token):
        data = generate_random_car_engines()
        random_id = random_car_engines_id(token)

        response = garage().put(f'/car_engines/{random_id}/',
                                headers={'Authorization': 'Bearer ' + token[0]},
                                data=data
                                )
        assert response.status_code == 200
        assert S(car_engines) == response.json()
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['volume'] == data['volume']
        assert response.json()['origin'] == data['origin']
        assert response.json()['production_year'] == data['production_year']

    def test_partial_update_car_engines(self, token):
        random_data = generate_random_car_engines()
        engine_number = random_data['engine_number']
        volume = random_data['volume']
        random_id = random_car_engines_id(token)

        data = {
            "engine_number": engine_number,
            "volume": volume,
        }
        response = garage().patch(f'/car_engines/{random_id}/',
                                  headers={'Authorization': 'Bearer ' + token[0]},
                                  data=data
                                  )
        assert response.status_code == 200
        assert S(car_engines) == response.json()
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['volume'] == data['volume']

    def test_delete_car_engines(self, token):
        random_id = random_car_engines_id(token)
        response = garage().delete(f'/car_engines/{random_id}/',
                                   headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 204
        assert response.text == ''
