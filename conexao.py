import mysql.connector
from mysql.connector import Error

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            database = "db_biblioteca",
            user= "root",
            password = ""
        )
        
        if conexao.is_connected():
            print("Conexão com o banco bem sucedida!")
            return conexao
        
    except Error as e:
        print(f"Erro na conexão com o banco {e}")
        return None