import os
from garage_api.utils.requests_helper import BaseSession
from dotenv import dotenv_values

dotenv = dotenv_values()


def garage_authorization() -> BaseSession:
    api_authorization = dotenv.get('API_AUTHORIZATION')
    return BaseSession(base_url=api_authorization)


def garage() -> BaseSession:
    api_url = dotenv.get('API_URL')
    return BaseSession(base_url=api_url)
