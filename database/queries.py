from database.connection import instance_cursor

def consulta(user):
    with instance_cursor() as db:
        query = '''
                SELECT nome, usuario, senha 
                FROM REGISTROS
                WHERE usuario = %s   
                '''
        db.execute_query(query, (user,))
        return db.fetchall()

def consulta_geral():
    with instance_cursor() as db:
        query = '''
                SELECT * 
                FROM REGISTROS   
                '''
        db.execute_query(query)
        return db.fetchall()

def add_registro(nome, user, senha):
    with instance_cursor() as db:
        query = '''
                INSERT INTO REGISTROS (nome, usuario, senha) VALUES (%s, %s, %s)
                '''
        db.execute_query(query, (nome, user, senha))
        db.commit()

def cria_tabela():
    with instance_cursor() as db:
        query = '''
                CREATE TABLE IF NOT EXISTS REGISTROS (
                    nome varchar(255),
                    usuario varchar(255),
                    senha varchar(255)
                )
                '''
        db.execute_query(query)
        db.commit()