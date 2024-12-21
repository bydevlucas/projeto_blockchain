from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)

# Instância da Blockchain
blockchain = Blockchain()

# Rota para obter todos os blocos
@app.route('/blocks', methods=['GET'])
def get_blocks():
    # Convertendo os blocos para dicionários para a resposta JSON
    chain = [block.__dict__ for block in blockchain.chain]
    return jsonify(chain), 200

# Rota para adicionar um novo bloco
@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.json
    certificates = data.get('certificates', [])

    # Verifica se a lista de certificados está vazia
    if not certificates:
        return jsonify({"error": "Certificados não fornecidos"}), 400

    # Adiciona os certificados na blockchain (assumindo que 'certificates' é uma lista de objetos)
    for certificate in certificates:
        blockchain.add_block(certificate)  # Aqui estamos passando o certificado diretamente

    # Verificar se a blockchain está válida após adicionar os blocos
    is_valid = blockchain.validate_chain()

    # Retorna a resposta
    return jsonify({
        "message": "Bloco(s) adicionado(s) com sucesso!",
        "blockchain_valid": is_valid
    }), 201

# Rota para validar a blockchain
@app.route('/validate', methods=['GET'])
def validate_chain():
    # Verifica se a blockchain é válida
    is_valid = blockchain.validate_chain()
    return jsonify({"valid": is_valid}), 200

# Rota para buscar um bloco específico
@app.route('/blocks/<int:index>', methods=['GET'])
def get_block(index):
    # Verifica se o índice do bloco é válido
    if index >= len(blockchain.chain) or index < 0:
        return jsonify({"error": "Bloco não encontrado"}), 404

    block = blockchain.chain[index]
    return jsonify(block.__dict__), 200

if __name__ == '__main__':
    # Inicializa a aplicação Flask com debug ativado e acessível em todas as interfaces (0.0.0.0)
    app.run(debug=True, host='0.0.0.0', port=5000)
