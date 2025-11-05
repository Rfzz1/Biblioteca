from conexao import criar_conexao

def cadastrar_funcionario(nome, usuario, senha):
    conexao = criar_conexao()
    if conexao is None:
        print("Erro: não foi possível conectar ao banco.")
        return

    try:
        cursor = conexao.cursor()

        insercao = "INSERT INTO tb_usuarios (nome, usuario, senha) VALUES (%s, %s, %s)"
        cursor.execute(insercao, (nome, usuario, senha))
        conexao.commit() 

        print("Funcionário cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro ao cadastrar funcionário: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()