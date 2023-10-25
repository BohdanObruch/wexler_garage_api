import pytest

from garage_api.utils.sessions import garage_authorization
from dotenv import dotenv_values, load_dotenv


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


dotenv = dotenv_values()

username = dotenv.get('USERNAME')
password = dotenv.get('PASSWORD')


@pytest.fixture()
def token():
    payload = {
        "username": username,
        "password": password
    }
    response = garage_authorization().post(f'/user/login/',
                                           data=payload)
    token = response.json()['access']
    refresh_token = response.json()['refresh']
    return token, refresh_token
