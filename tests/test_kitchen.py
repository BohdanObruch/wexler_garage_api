from garage_api.utils.sessions import garage


class TestKitchen:
    def test_brew_coffee_in_coffee_maker_list(self, token):
        response = garage().get('/kitchen/brew_coffee_in_coffee_maker',
                                headers={'Authorization': 'Bearer ' + token[0]}
                                )
        assert 'result' in response.json()
        if response.status_code == 201:
            assert response.json()['result'] == 'Кофе сварен!'
        elif response.status_code == 503:
            result = response.json()['result']
            assert result in ['Сервер кофе недоступен', 'Все занято, приходите позже',
                              'Кофе тут не наливают (временно), попробуйте снова',
                              'Все кофеварки заняты, пейте чай!']
