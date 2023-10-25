import json

from garage_api.utils.sessions import garage
from tests.conftest import dotenv
import requests

username = dotenv.get('USERNAME')
password = dotenv.get('PASSWORD')


def test_token():
    payload = {
        "username": username,
        "password": password
    }
    responce = garage().post(f'/user/login/',
                             data=payload)
    print(responce.json()['access'])

