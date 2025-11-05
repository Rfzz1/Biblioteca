from conexao import criar_conexao

def receber_livro(titulo):
    conexao = criar_conexao()
    if conexao is None:
        return
    try:
        cursor = conexao.cursor()

        # Verifica se o livro está emprestado
        consulta = "SELECT e.id_livro FROM tb_emprestimos e JOIN tb_livros l ON e.id_livro = l.id WHERE l.titulo = %s AND e.devolvido = 0"
        cursor.execute(consulta, (titulo,))
        resultado = cursor.fetchone()

        if not resultado:
            print("Esse livro não está emprestado ou já foi devolvido.")
            return
        id_livro = resultado[0]
        
        # Atualiza o empréstimo como devolvido
        cursor.execute("UPDATE tb_emprestimos SET devolvido = 1 WHERE id_livro = %s AND devolvido = 0", (id_livro,))
        conexao.commit()
        
        # Aumenta a quantidade de exemplares disponíveis
        quantidade = "UPDATE tb_livros SET quantidade = quantidade + 1 WHERE id_livro = %s"
        cursor.execute(
            quantidade,(id_livro,))
        conexao.commit()
        print("Livro devolvido com sucesso!")

    except Exception as e:
        print(f"Erro ao devolver o livro: {e}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
