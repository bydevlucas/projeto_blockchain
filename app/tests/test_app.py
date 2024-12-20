<<<<<<< HEAD
import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        """Configurar o Flask test client antes de cada teste."""
        self.app = app.test_client()
        self.app.testing = True

    def test_get_blocks(self):
        """Testar a rota GET /blocks para verificar se os blocos são retornados corretamente."""
        response = self.app.get('/blocks')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"certificates" in response.data)  # Verificando se o campo certificates está presente na resposta

    def test_add_block(self):
        """Testar a rota POST /add_block para adicionar um novo bloco."""
        new_block = {
            "certificates": [
                {"Certificado": "Diploma", "Instituição": "IFG", "Ano": "2024", "Titular": "Lucas"}
            ]
        }
        response = self.app.post('/add_block', data=json.dumps(new_block), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Bloco adicionado com sucesso!", response.data)

    def test_validate_chain(self):
        """Testar a rota GET /validate para validar a blockchain."""
        response = self.app.get('/validate')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"valid", response.data)

    def test_get_block(self):
        """Testar a rota GET /blocks/<index> para obter um bloco específico."""
        response = self.app.get('/blocks/0')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"certificates", response.data)
        
        # Testar se um bloco inexistente retorna o erro 404
        response = self.app.get('/blocks/999')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
=======
import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        """Configurar o Flask test client antes de cada teste."""
        self.app = app.test_client()
        self.app.testing = True

    def test_get_blocks(self):
        """Testar a rota GET /blocks para verificar se os blocos são retornados corretamente."""
        response = self.app.get('/blocks')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"certificates" in response.data)  # Verificando se o campo certificates está presente na resposta

    def test_add_block(self):
        """Testar a rota POST /add_block para adicionar um novo bloco."""
        new_block = {
            "certificates": [
                {"Certificado": "Diploma", "Instituição": "IFG", "Ano": "2024", "Titular": "Lucas"}
            ]
        }
        response = self.app.post('/add_block', data=json.dumps(new_block), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Bloco adicionado com sucesso!", response.data)

    def test_validate_chain(self):
        """Testar a rota GET /validate para validar a blockchain."""
        response = self.app.get('/validate')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"valid", response.data)

    def test_get_block(self):
        """Testar a rota GET /blocks/<index> para obter um bloco específico."""
        response = self.app.get('/blocks/0')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"certificates", response.data)
        
        # Testar se um bloco inexistente retorna o erro 404
        response = self.app.get('/blocks/999')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
>>>>>>> dcaf25c5e5290811ee816302ff867b98749dd2ca
