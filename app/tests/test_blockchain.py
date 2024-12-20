import unittest
from app.blockchain import Blockchain, Block

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        """Método para configurar a instância de Blockchain antes de cada teste."""
        self.blockchain = Blockchain()

    def test_genesis_block(self):
        """Testar se o bloco gênesis é criado corretamente."""
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0].previous_hash, "0")

    def test_add_block(self):
        """Testar se novos blocos são adicionados corretamente."""
        block_data = {"Certificado": "Diploma", "Instituição": "IFG", "Ano": "2024", "Titular": "Lucas"}
        self.blockchain.add_block([block_data])
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(self.blockchain.chain[-1].certificates, [block_data])

    def test_validate_chain_valid(self):
        """Testar se a blockchain é válida após adicionar blocos corretamente."""
        block_data = {"Certificado": "Diploma", "Instituição": "IFG", "Ano": "2024", "Titular": "Lucas"}
        self.blockchain.add_block([block_data])
        self.assertTrue(self.blockchain.validate_chain())

    def test_validate_chain_invalid(self):
        """Testar se a blockchain é invalidada quando o hash de um bloco é alterado."""
        block_data = {"Certificado": "Diploma", "Instituição": "IFG", "Ano": "2024", "Titular": "Lucas"}
        self.blockchain.add_block([block_data])
        
        # Manipular o hash para invalidar a blockchain
        self.blockchain.chain[1].certificates = {"Certificado": "Falso"}
        self.assertFalse(self.blockchain.validate_chain())

if __name__ == "__main__":
    unittest.main()
