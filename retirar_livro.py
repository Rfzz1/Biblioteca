from conexao import criar_conexao
from datetime import date, timedelta

def retirar_livro(titulo, cpf_leitor):
    conexao = criar_conexao()
    if conexao is None:
        print("Erro: não foi possível conectar ao banco.")
        return False

    try:
        cursor = conexao.cursor(dictionary=True)

        #Verifica o leitor pelo CPF
        cursor.execute("SELECT * FROM tb_leitores WHERE cpf = %s", (cpf_leitor,))
        leitor = cursor.fetchone()

        if not leitor:
            print("Leitor não encontrado.")
            return False

        #Verifica o livro
        cursor.execute("SELECT * FROM tb_livros WHERE titulo = %s", (titulo,))
        livro = cursor.fetchone()

        if not livro:
            print("Livro não encontrado no acervo.")
            return False

        if livro['quantidade'] <= 0:
            print("Não há exemplares disponíveis para empréstimo.")
            return False

        #Registra o empréstimo
        data_emprestimo = date.today()

        cursor.execute("""
            INSERT INTO tb_emprestimos (id_livro, id_leitor, data_emprestimo, devolvido)
            VALUES (%s, %s, %s, 0)
        """, (livro['id'], leitor['id'], data_emprestimo))
        conexao.commit()

        #Atualiza quantidade
        cursor.execute("UPDATE tb_livros SET quantidade = quantidade - 1 WHERE id = %s", (livro['id'],))
        conexao.commit()

        print(f"Livro '{livro['titulo']}' emprestado com sucesso para {leitor['nome']}!")
        return True

    except Exception as e:
        print(f"Erro ao retirar livro: {e}")
        return False

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
