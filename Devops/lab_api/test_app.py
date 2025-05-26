import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn("items", response.json)
        self.assertIsInstance(response.json["items"], list)

    def test_protected_with_token(self):
        # Primeiro, gera o token
        login_response = self.client.post('/login')
        token = login_response.json.get('access_token')

        # Usa o token na requisição protegida
        headers = {
            "Authorization": f"Bearer {token}"
        }
        protected_response = self.client.get('/protected', headers=headers)
        self.assertEqual(protected_response.status_code, 200)
        self.assertEqual(protected_response.json["message"], "Protected route")

    def test_invalid_route(self):
        response = self.client.get('/rota-inexistente')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
