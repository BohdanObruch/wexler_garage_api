from pytest import mark
from garage_api.schemas.garage import root
from garage_api.utils.sessions import garage
from pytest_voluptuous import S


class TestRoot:

    @mark.testomatio('@T966ebf01')
    def test_root_list(self, token):
        response = garage().get(
            '/root/', headers={'Authorization': 'Bearer ' + token[0]})
        assert response.status_code == 200
        assert S(root) == response.json()
        assert '/cars/' in response.json()['cars']
        assert '/customers/' in response.json()['customers']
        assert '/car_engines/' in response.json()['car_engines']
        assert '/operations/' in response.json()['operations']
        assert '/services/' in response.json()['services']
        assert '/payments/' in response.json()['payments']
