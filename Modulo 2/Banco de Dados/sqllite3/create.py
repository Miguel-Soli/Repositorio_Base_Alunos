import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_conection():
    return sq.connect(DB_PATH)

def criar_tabela(): 
    with get_conection() as conn:
        conn.execute( '''
        CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE,
            curso TEXT
            );
       ''')
        

def inserir_aluno(name,age,email,curso):
    with get_conection() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO alunos (name,age,email,curso) VALUES (?,?,?,?)',(name,age,email,curso))
        conn.commit()
        return cur.lastrowid
    
if __name__ == '__main__':
    criar_tabela()
    #bem vindo ao banco de dados
    print("### BEM VINDO AO DE DADOS ###")
    name =  input("Digite o nome do aluno: ")
    age =  int(input("Digite a idade  do aluno: "))
    email=  input("Digite o email: ")
    curso=  input("Digite o curso: ")

    novo_id = inserir_aluno(name,age,email,curso)
    