import sqlite3 as sq 

DB_PATH = 'aluno.db'

def get_connection():
    return sq.connect(DB_PATH)

def criar_tabela():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,    
                idade INTEGER,
                email TEXT UNIQUE,
                curso TEXT
            );
        ''')

def inserir_aluno(nome,idade,email,curso):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO alunos (nome,idade,email,curso) VALUES (?, ?, ?, ?)', (nome,idade,email,curso))
        conn.commit()
        return cur.lastrowid
    
if __name__ == '__main__':
    criar_tabela()
    print("### BEM VINDO AO BANCO DE DADOS ###")
    nome_aluno = input("Digite seu nome: ")
    idade_aluno = int(input("Digite sua idade: "))
    email_aluno = input("Digite seu email: ")
    curso_aluno = input("Digite o nome do curso: ")
    
    novo_id = inserir_aluno(nome_aluno,idade_aluno,email_aluno,curso_aluno)

    print(f"Aluno inserido no sistema id = {novo_id}")
