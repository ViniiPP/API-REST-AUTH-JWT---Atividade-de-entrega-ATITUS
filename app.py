from flask import Flask, request, jsonify
from database import GerenciadorDeDados
from auth import configurar_autenticacao, jwt, gerar_hash_senha, verificar_senha
from flask_jwt_extended import create_access_token, jwt_required
import sqlite3

app = Flask(__name__)
configurar_autenticacao(app)
gerenciador = GerenciadorDeDados()
gerenciador.inicializar_banco()

# Rotas de autenticação
@app.route('/registro', methods=['POST'])
def registrar():
    dados = request.get_json()
    if not dados or 'nome_usuario' not in dados or 'senha' not in dados:
        return jsonify({"mensagem": "Dados incompletos"}), 400
    
    try:
        hash_senha = gerar_hash_senha(dados['senha'])
        gerenciador.criar_usuario(dados['nome_usuario'], hash_senha)
        return jsonify({"mensagem": "Usuário criado"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"mensagem": "Nome de usuário já existe"}), 409

@app.route('/login', methods=['POST'])
def logar():
    dados = request.get_json()
    usuario = gerenciador.obter_usuario_por_nome(dados.get('nome_usuario'))
    
    if usuario and verificar_senha(dados.get('senha'), usuario[2]):
        token_acesso = create_access_token(identity=str(usuario[1]))
        return jsonify(token_acesso=token_acesso), 200
    
    return jsonify({"mensagem": "Credenciais inválidas"}), 401

# Rotas protegidas
@app.route('/dados', methods=['POST'])
@jwt_required()
def adicionar_dado():
    dados = request.get_json()
    if not dados or 'valor' not in dados or len(dados['valor']) > 255:
        return jsonify({"erro": "Dados inválidos"}), 400
    
    novo_id = gerenciador.criar_dado(dados['valor'])
    return jsonify({"id": novo_id}), 201

@app.route('/dados', methods=['GET'])
@jwt_required()
def obter_dados():
    dados = gerenciador.obter_todos_dados()
    return jsonify([{"id": linha[0], "valor": linha[1], "data_criacao": linha[2]} for linha in dados]), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)