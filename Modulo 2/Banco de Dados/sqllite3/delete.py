import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_conection():
    return sq.connect(DB_PATH)

def deletar_aluno(id):
    with get_conection() as conn:
        cursor = conn.execute(
            ''' 
            DELETE FROM alunos
            WHERE id = ?
            ''',
            (id,)
         )
        return cursor.rowcount > 0 
    
if __name__ == '__main__':
    print("###DELETAR USUÁRIO ###")
    id = int(input("Digite o id do usuário: "))

    deletar_aluno(id)