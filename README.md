# API REST com Autenticação JWT - Atividade de Entrega ATITUS

Esta é uma API REST simples desenvolvida com Flask que implementa autenticação usando JWT (JSON Web Tokens) e armazenamento de dados em SQLite.

## Integrantes
-    Vinícius Pereira Polli (RA: 1136503);
-    Laura Schu (RA: 1134656).


## 🚀 Funcionalidades

- Registro de usuários
- Autenticação com JWT
- Armazenamento de dados com SQLite
- Rotas protegidas
- Gerenciamento de dados (criar e listar)

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure o arquivo `.env`:
   Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```env
JWT_SECRET_KEY=sua_chave_secreta_muito_segura_123
```

## 🛠️ Estrutura do Projeto

```
.
├── app.py              # Arquivo principal da aplicação
├── auth.py            # Configurações de autenticação
├── database.py        # Gerenciamento do banco de dados
├── requirements.txt   # Dependências do projeto
├── .env              # Variáveis de ambiente
└── dados.db          # Banco de dados SQLite (criado automaticamente)
```

## 🚀 Como Executar

- Inicie o servidor:

```bash
python app.py
```

O servidor estará rodando em `http://localhost:5000`

## 📝 Endpoints

### Autenticação

#### Registro de Usuário

```bash
POST /registro
Content-Type: application/json

{
    "nome_usuario": "seu_usuario",
    "senha": "sua_senha"
}
```

#### Login

```bash
POST /login
Content-Type: application/json

{
    "nome_usuario": "seu_usuario",
    "senha": "sua_senha"
}
```

### Dados (Protegidos)

#### Criar Dado

```bash
POST /dados
Authorization: Bearer seu_token_jwt
Content-Type: application/json

{
    "valor": "seu_dado"
}
```

#### Listar Dados

```bash
GET /dados
Authorization: Bearer seu_token_jwt
```

## 🔒 Segurança

- Todas as senhas são armazenadas com hash usando PBKDF2-SHA256
- Rotas protegidas requerem token JWT válido
- Tokens JWT expiram após 15 minutos (configurável)
- Chave secreta JWT configurável via variável de ambiente

## 🛡️ Exemplos de Uso

### Registro de Usuário

```bash
curl -X POST http://localhost:5000/registro \
     -H "Content-Type: application/json" \
     -d "{\"nome_usuario\":\"teste\",\"senha\":\"123456\"}"
```

### Login

```bash
curl -X POST http://localhost:5000/login \
     -H "Content-Type: application/json" \
     -d "{\"nome_usuario\":\"teste\",\"senha\":\"123456\"}"
```

### Criar Dado (com token)

```bash
curl -X POST http://localhost:5000/dados \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer seu_token_jwt" \
     -d "{\"valor\":\"teste de dados\"}"
```

### Listar Dados (com token)

```bash
curl -X GET http://localhost:5000/dados \
     -H "Authorization: Bearer seu_token_jwt"
```

## 📚 Dependências

- Flask==2.0.1
- Flask-JWT-Extended==4.3.1
- Passlib==1.7.4
- Python-dotenv==0.19.0

