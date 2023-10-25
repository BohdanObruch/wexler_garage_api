from garage_api.utils.sessions import garage_authorization
from tests.conftest import username, password
from pytest_voluptuous import S
from garage_api.schemas.garage import user_login, refresh_token


class TestUser:
    def test_user_login(self):
        payload = {
            "username": username,
            "password": password
        }
        response = garage_authorization().post(f'/user/login/',
                                               data=payload)
        assert response.status_code == 200
        assert S(user_login) == response.json()

    def test_login_refreh(self, token):
        data = {
            "refresh": token[1]
        }
        response = garage_authorization().post(f'/user/login/refresh/',
                                               data=data)
        assert response.status_code == 200
        assert S(refresh_token) == response.json()
