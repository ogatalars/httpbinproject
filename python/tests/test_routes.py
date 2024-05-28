import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.from_object('config.TestingConfig')
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to my httpbin-like API", response.data)

    def test_get_request(self):
        response = self.client.get('/get?name=John&age=30')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['args']['name'], 'John')
        self.assertEqual(json_data['args']['age'], '30')

    def test_post_request(self):
        response = self.client.post('/post', data={'name': 'John', 'age': '30'})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['form']['name'], 'John')
        self.assertEqual(json_data['form']['age'], '30')

    def test_headers(self):
        response = self.client.get('/headers')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn('User-Agent', json_data)

    def test_status(self):
        response = self.client.get('/status/418')
        self.assertEqual(response.status_code, 418)

if __name__ == '__main__':
    unittest.main()
