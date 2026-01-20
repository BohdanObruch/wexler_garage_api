import os
import pytest
from dotenv import load_dotenv

from garage_api.utils.sessions import garage_authorization

load_dotenv()

username = os.getenv('API_USERNAME')
password = os.getenv('API_PASSWORD')


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