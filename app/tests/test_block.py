import unittest
from datetime import datetime
from app.blockchain import Block

class TestBlock(unittest.TestCase):

    def setUp(self):
        self.certificates = {"Certificado": "Diploma", "Instituição": "Exemplo", "Ano": "2024", "Titular": "Test User"}
        self.previous_hash = "0"

    def test_generate_hash_length(self):
        block = Block(self.certificates, self.previous_hash)
        self.assertEqual(len(block.hash), 64, "O hash gerado deve ter 64 caracteres.")

    def test_generate_hash_uniqueness(self):
        block1 = Block(self.certificates, self.previous_hash)
        block2 = Block(self.certificates, self.previous_hash)
        self.assertNotEqual(block1.hash, block2.hash, "Hashes devem ser únicos devido ao timestamp.")

    def test_block_content(self):
        block = Block(self.certificates, self.previous_hash)
        self.assertEqual(block.certificates, self.certificates, "Os certificados devem ser atribuídos corretamente.")
        self.assertEqual(block.previous_hash, self.previous_hash, "O hash anterior deve ser atribuído corretamente.")

    def test_generate_hash_length(self):
        block = Block(self.certificates, self.previous_hash)
        self.assertEqual(len(block.hash), 64, "O hash gerado deve ter 64 caracteres.")


if __name__ == "__main__":
    unittest.main()
