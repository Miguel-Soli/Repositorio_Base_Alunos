import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_conection():
    return sq.connect(DB_PATH)

def atualizar_aluno(nome,idade,email,curso):
    with get_conection() as conn:
         cursor = conn.execute(
            ''' 
            UPDATE alunos
            SET email = nome= ?, idade = ?, email = ?, curso = ?
            WHERE id = ?;
            ''',
            (nome,idade,email,curso,id,)
         )
         conn.commit()
         return cursor.rowcount
    
if __name__ == '__main__':
    
    #bem vindo ao banco de dados
    print("### BEM VINDO AO DE DADOS ###")
    id =  int(input("Digite o ID para alterar: "))
    nome =  input("Digite o nome do aluno: ")
    idade =  int(input("Digite a idade  do aluno: "))
    email=  input("Digite o email: ")
    curso=  input("Digite o curso: ")
   
 