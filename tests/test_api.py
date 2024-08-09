from run import app

class TestAPI:

    # API тесты для списка постов
    def test_api_get_all(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "проверяем статус страницы"
        assert response.mimetype == "application/json"

    def test_api_get_all_type_and_count(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, "проверяем что выдаются данные типа list"
        assert len(response.json) == 8, "срисок состоит из 8 элементов"

    def test_api_get_all_check_data(self, keys_should_be):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        first_keys = set(response.json[0].keys())
        assert first_keys == keys_should_be, "Не правильный набор ключей"

    # API тесты для 1 поста

    def test_api_get_one(self):
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert response.status_code == 200, "проверяем статус страницы"
        assert response.mimetype == "application/json"

    def test_api_get_one_type_and_count(self):
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert type(response.json) == dict, "проверяем что выдаются данные типа list"

    def test_api_get_one_check_data(self, keys_should_be):
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        first_keys = set(response.json.keys())
        assert first_keys == keys_should_be, "Не правильный набор ключей"


