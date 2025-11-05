from conexao import criar_conexao

def cadastrar_usuario(nome, cpf, data_nascimento, email, telefone):
    conexao = criar_conexao()
    if conexao is None:
        print("Erro: não foi possível conectar ao banco.")
        return

    try:
        cursor = conexao.cursor()

        insercao = "INSERT INTO tb_leitores (nome, cpf, data_nascimento, email, telefone) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insercao, (nome, cpf, data_nascimento, email, telefone))
        conexao.commit() 

        print("Usuário cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
