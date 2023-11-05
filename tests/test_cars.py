from pytest import mark
from garage_api.data.fake_data import random_cars
from garage_api.schemas.garage import cars_list, car, car_info
from garage_api.utils.sessions import garage
from pytest_voluptuous import S
from garage_api.helpers import app


class TestCars:

    @mark.testomatio('@Tf5e37e56')
    def test_list_cars(self, token):
        response = garage().get(
            '/cars/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(cars_list) == response.json()
        assert response.json()['count'] == len(response.json()['results'])

    @mark.testomatio('@Tf50a6c4c')
    def test_create_cars_post(self, token):
        data = random_cars(token)
        response = garage().post(
            '/cars/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 201
        assert S(car) == response.json()
        assert response.json()['plate_number'] == data['plate_number']
        assert response.json()['brand'] == data['brand']
        assert response.json()['model'] == data['model']
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['car_owner'] == data['car_owner']

    @mark.testomatio('@Tb3a27beb')
    def test_create_cars_put(self, token):
        data = random_cars(token)
        response = garage().put(
            '/cars/put/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 201
        assert S(car) == response.json()
        assert response.json()['plate_number'] == data['plate_number']
        assert response.json()['brand'] == data['brand']
        assert response.json()['model'] == data['model']
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['car_owner'] == data['car_owner']

    @mark.testomatio('@T9833f7b0')
    def test_details_by_random_car(self, token):
        car_id = app.cars.random_car_id(token)
        response = garage().get(
            f'/cars/{car_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(car_info) == response.json()
        assert response.json()['id'] == car_id

    @mark.testomatio('@Tbb53686a')
    def test_update_cars(self, token):
        data = random_cars(token)
        car_id = app.cars.random_car_id(token)
        response = garage().put(
            f'/cars/{car_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(car) == response.json()
        assert response.json()['id'] == car_id
        assert response.json()['plate_number'] == data['plate_number']
        assert response.json()['brand'] == data['brand']
        assert response.json()['model'] == data['model']
        assert response.json()['engine_number'] == data['engine_number']
        assert response.json()['car_owner'] == data['car_owner']

    @mark.testomatio('@T71ee668a')
    def test_partial_update_cars(self, token):
        random_data = random_cars(token)
        plate_number = random_data['plate_number']
        model = random_data['model']
        car_owner = random_data['car_owner']
        data = {'plate_number': plate_number,
                'model': model, 'car_owner': car_owner}
        car_id = app.cars.random_car_id(token)
        response = garage().put(
            f'/cars/{car_id}/', headers={'Authorization': 'Bearer ' + token[0]}, data=data)
        assert response.status_code == 200
        assert S(car) == response.json()
        assert response.json()['id'] == car_id
        assert response.json()['plate_number'] == data['plate_number']
        assert response.json()['model'] == data['model']
        assert response.json()['car_owner'] == data['car_owner']

    @mark.testomatio('@Te2c20bd1')
    def test_delete_cars(self, token):
        car_id = app.cars.random_car_id(token)
        response = garage().delete(
            f'/cars/{car_id}/', headers={'Authorization': 'Bearer ' + token[0]})
        if response.status_code == 204:
            assert response.content == b''
