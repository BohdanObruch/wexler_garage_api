import pytest

from garage_api.utils.sessions import garage_authorization
from dotenv import load_dotenv
import os


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


@pytest.fixture()
def token():
    payload = {
        "username": username,
        "password": password
    }
    response = garage_authorization().post(f'/user/login/',
                                           data=payload)
    print(username)
    print(password)
    token = response.json()['access']
    refresh_token = response.json()['refresh']
    print(token)
    print(refresh_token)
    return token, refresh_token
