# Importar as classes necessárias
from app.blockchain import Blockchain

def main():
    # Criar instância da blockchain
    local_blockchain = Blockchain()

    # Certificados para adicionar
    block_one = {
        "Certificado": "Diploma",
        "Instituição": "Instituto Federal de Goiás - Campus Formosa",
        "Ano": "2024",
        "Titular": "Lucas da Silva Rodrigues"
    }

    fake_certificate = {
        "Certificado": "Diploma",
        "Instituição": "Universidade Federal de Minas Gerais - Campus Pampulha",
        "Ano": "2023",
        "Titular": "Carlos, Mariana Alves Souza"
    }

    # Adicionar os certificados
    print("Adicionando o primeiro certificado...")
    local_blockchain.add_block(block_one)  # Passa o certificado diretamente, não dentro de uma lista
    print("Adicionando o certificado falso...")
    local_blockchain.add_block(fake_certificate)  # Passa o certificado diretamente

    # Imprimir a blockchain
    print("\nBlockchain atual:")
    local_blockchain.print_blocks()

    # Validar a blockchain
    is_valid = local_blockchain.validate_chain()
    print(f"\nA blockchain é válida? {'Sim' if is_valid else 'Não'}")

if __name__ == "__main__":
    main()
