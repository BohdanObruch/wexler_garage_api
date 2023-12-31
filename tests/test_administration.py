from pytest import mark
from garage_api.utils.sessions import garage
from tests.conftest import username
from pytest_voluptuous import S
from garage_api.schemas.garage import administration


class TestAdministration:

    @mark.testomatio('@Tc8de47a0')
    def test_administration(self, token):
        headers = {'Authorization': 'Bearer ' + token[0]}
        response = garage().get('/administration/create_dataset', headers=headers)
        assert response.status_code == 201
        assert response.json()['status'] == 'SUCCESS'
        assert response.json()[
            'message'] == f'Dataset for user {username} created successfully'
        assert S(administration) == response.json()
