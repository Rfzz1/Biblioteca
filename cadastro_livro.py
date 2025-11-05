from conexao import criar_conexao

def cadastrar_livro(titulo, autor, isbn, quantidade):
    conexao = criar_conexao()
    if conexao is None:
        print("Erro: não foi possível conectar ao banco.")
        return

    try:
        cursor = conexao.cursor()

        insercao = "INSERT INTO tb_livros (titulo, autor, isbn, quantidade) VALUES (%s, %s, %s, %s)"
        cursor.execute(insercao, (titulo, autor, isbn, quantidade))
        conexao.commit() 

        print("Livro cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro ao cadastrar livro: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()