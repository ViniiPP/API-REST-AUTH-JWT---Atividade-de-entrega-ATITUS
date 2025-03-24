from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from passlib.hash import pbkdf2_sha256
import os

jwt = JWTManager()

def configurar_autenticacao(app):
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "chave_segura")
    jwt.init_app(app)

def verificar_senha(senha, hash):
    return pbkdf2_sha256.verify(senha, hash)

def gerar_hash_senha(senha):
    return pbkdf2_sha256.hash(senha)
