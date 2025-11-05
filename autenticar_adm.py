from conexao import criar_conexao
def autenticar_adm(login,senha):
    conexao=criar_conexao()
    if conexao is None:
        return False
    try:
        cursor = conexao.cursor()
        
        #Proteção contra Injection
        consulta = "SELECT * FROM tb_usuarios WHERE usuario = %s AND senha = %s"
        cursor.execute(consulta, (login,senha)) 
        
        resultado = cursor.fetchone()
        
        if resultado:
            return True #Usuario encontrado
        else:
            return False #Usuário ou senha incorretos
        
    finally:
        #Fecha a conexão
        if conexao.is_connected():
            cursor.close()
            conexao.close()