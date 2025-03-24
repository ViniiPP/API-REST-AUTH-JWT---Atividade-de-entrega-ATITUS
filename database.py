import sqlite3
from contextlib import contextmanager

class GerenciadorDeDados:
    def __init__(self, nome_do_banco='dados.db'):
        self.nome_do_banco = nome_do_banco

    @contextmanager
    def obter_cursor(self):
        conexao = sqlite3.connect(self.nome_do_banco)
        cursor = conexao.cursor()
        try:
            yield cursor
            conexao.commit()
        finally:
            conexao.close()

    def inicializar_banco(self):
        with self.obter_cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS dados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    valor TEXT NOT NULL,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_usuario TEXT UNIQUE NOT NULL,
                    hash_senha TEXT NOT NULL
                )''')

    def criar_dado(self, valor):
        with self.obter_cursor() as cursor:
            cursor.execute('INSERT INTO dados (valor) VALUES (?)', (valor,))
            return cursor.lastrowid

    def obter_todos_dados(self):
        with self.obter_cursor() as cursor:
            cursor.execute('SELECT * FROM dados ORDER BY data_criacao DESC')
            return cursor.fetchall()

    def criar_usuario(self, nome_usuario, hash_senha):
        with self.obter_cursor() as cursor:
            cursor.execute('INSERT INTO usuarios (nome_usuario, hash_senha) VALUES (?, ?)', 
                         (nome_usuario, hash_senha))
            return cursor.lastrowid

    def obter_usuario_por_nome(self, nome_usuario):
        with self.obter_cursor() as cursor:
            cursor.execute('SELECT * FROM usuarios WHERE nome_usuario = ?', (nome_usuario,))
            return cursor.fetchone()
