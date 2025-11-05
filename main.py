from autenticar import autenticar_usuario
from cadastro import cadastrar_usuario
from autenticar_func import autenticar_funcionario
from cadastro_func import cadastrar_funcionario
from autenticar_adm import autenticar_adm
from cadastro_livro import cadastrar_livro
from remover_livro import remover_livro
from devolvido import receber_livro
from retirar_livro import retirar_livro
import os
import time


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# ---------------------- PROGRAMA PRINCIPAL ----------------------
if __name__ == "__main__":
    while True:
        print("=== Sistema Biblioteca ===\n")
        print("1 - Login ADM")
        print("2 - Login Funcionário")
        print("3 - Cadastro Leitor")
        print("4 - Login Leitor")
        print("0 - Encerrar")
        opcao = input("Escolha sua opção: ").strip()
        limpar_tela()

        # ---------------------- ADM ----------------------
        if opcao == "1":
            usuario_input = input("Digite seu usuário:\n")
            senha_input = input("Digite sua senha:\n")

            if autenticar_adm(usuario_input, senha_input):
                print("Login efetuado com sucesso!")
                time.sleep(1)
                limpar_tela()

                while True:
                    print("=== Menu Administrador ===")
                    print("1 - Cadastrar novo funcionário")
                    print("0 - Voltar ao menu principal")
                    sub_opcao = input("Escolha: ").strip()
                    limpar_tela()

                    if sub_opcao == "1":
                        nome = input("Nome do funcionário:\n")
                        usuario = input("Usuário do funcionário:\n")
                        senha = input("Senha do funcionário:\n")
                        cadastrar_funcionario(nome, usuario, senha)
                        time.sleep(2)
                        limpar_tela()

                    elif sub_opcao == "0":
                        print("Saindo do menu administrador...\n")
                        time.sleep(1)
                        limpar_tela()
                        break
                    else:
                        print("Opção inválida!\n")
                        time.sleep(2)
                        limpar_tela()
            else:
                print("Login ou senha incorretos!")
                time.sleep(2)
                limpar_tela()

        # ---------------------- FUNCIONÁRIO ----------------------
        elif opcao == "2":
            funcionario_input = input("Usuário:\n")
            senha_input = input("Senha:\n")

            if autenticar_funcionario(funcionario_input, senha_input):
                print("Login efetuado com sucesso!")
                time.sleep(1)
                limpar_tela()

                while True:
                    print("=== Menu Funcionário ===")
                    print("1 - Cadastrar novo livro")
                    print("2 - Receber devolução de livro")
                    print("3 - Remover livro da biblioteca")
                    print("0 - Voltar ao menu principal")
                    sub_opcao = input("Escolha: ").strip()
                    limpar_tela()

                    if sub_opcao == "1":
                        print("Cadastro de Livro\n")
                        titulo = input("Título do livro:\n")
                        autor = input("Autor(a):\n")
                        isbn = input("Código ISBN:\n")
                        quantidade = int(input("Quantidade de exemplares:\n"))
                        cadastrar_livro(titulo, autor, isbn, quantidade)
                        time.sleep(2)
                        limpar_tela()

                    elif sub_opcao == "2":
                        print("Receber livro devolvido\n")
                        titulo = input("Título completo do livro:\n")
                        receber_livro(titulo)
                        time.sleep(2)
                        limpar_tela()

                    elif sub_opcao == "3":
                        print("Remover Livro da Biblioteca\n")
                        isbn = input("Digite o código ISBN do livro:\n")
                        remover_livro(isbn)
                        time.sleep(2)
                        limpar_tela()

                    elif sub_opcao == "0":
                        print("Saindo do menu funcionário...\n")
                        time.sleep(1)
                        limpar_tela()
                        break
                    else:
                        print("Opção inválida!\n")
                        time.sleep(2)
                        limpar_tela()
            else:
                print("Login ou senha incorretos!")
                time.sleep(2)
                limpar_tela()

        # ---------------------- LEITOR ----------------------
        elif opcao == "3":
            print("Cadastro de Leitor\n")
            nome = input("Nome:\n")
            cpf = input("CPF (xxx.xxx.xxx-xx):\n")
            data_nascimento = input("Data de nascimento (YYYY-MM-DD):\n")
            email = input("E-mail:\n")
            telefone = input("Telefone:\n")
            cadastrar_usuario(nome, cpf, data_nascimento, email, telefone)
            print("Leitor cadastrado com sucesso!")
            time.sleep(2)
            limpar_tela()

        elif opcao == "4":
            print("Login do Leitor\n")
            cliente_login = input("Digite seu CPF (xxx.xxx.xxx-xx):\n")

            if autenticar_usuario(cliente_login):
                print("Login efetuado com sucesso!")
                time.sleep(1)
                limpar_tela()

                print("Retirar livros da biblioteca:\n")
                titulo = input("Qual título deseja retirar?\n")
                retirar_livro(titulo, cliente_login)
                time.sleep(2)
                limpar_tela()
            else:
                print("CPF não encontrado!")
                time.sleep(2)
                limpar_tela()

        elif opcao == "0":
            print("Encerrando o sistema...")
            time.sleep(1)
            break

        else:
            print("Opção inválida!\n")
            time.sleep(2)
            limpar_tela()
