import os
from garage_api.utils.requests_helper import BaseSession


def garage() -> BaseSession:
    api_url = os.getenv('API_URL')
    return BaseSession(base_url=api_url)
