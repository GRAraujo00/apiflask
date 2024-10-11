from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita o CORS

# Exemplo de lista de produtos
produtos = [
    {"id": 1, "nome": "Monobloco", "preco": 10.99},
    {"id": 2, "nome": "Caderno", "preco": 19.99},
    {"id": 3, "nome": "Caneta", "preco": 5.99},
]

# Rota para listar produtos (GET)
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

# Rota para adicionar um novo produto (POST)
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    # Recebe os dados enviados pelo aplicativo (nome e preco do produto)
    novo_produto = request.get_json()

    # Validação básica para garantir que 'nome' e 'preco' estão presentes
    if 'nome' not in novo_produto or 'preco' not in novo_produto:
        return jsonify({"erro": "Faltando campos obrigatórios"}), 400

    # Cria um novo ID incremental para o produto
    novo_produto['id'] = len(produtos) + 1

    # Adiciona o novo produto à lista
    produtos.append(novo_produto)

    # Retorna uma resposta de sucesso
    return jsonify(novo_produto), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
