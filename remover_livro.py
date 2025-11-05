from conexao import criar_conexao
def remover_livro(isbn):
    conexao=criar_conexao()
    if conexao is None:
        return False
    try:
        cursor = conexao.cursor()
        
        #Proteção contra Injection
        consulta = "SELECT * FROM tb_livros WHERE isbn = %s"
        cursor.execute(consulta, (isbn,)) 
        livro = cursor.fetchone()
        
        if not livro:
            print("Livro não encontrado no acervo.")
            return False
        
        # Confirma a exclusão
        deletar = "DELETE FROM tb_livros WHERE isbn = %s"
        cursor.execute(deletar, (isbn,))
        conexao.commit()
        
        print("Livro removido com sucesso!")
        return True
    
    except Exception as e:
        print(f"Erro ao remover livro: {e}")
        return False
        
    finally:
        #Fecha a conexão
        if conexao.is_connected():
            cursor.close()
            conexao.close()