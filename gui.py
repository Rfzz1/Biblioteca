import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

# ----------------- CONFIGURAÇÕES -----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ----------------- BANCO -----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_biblioteca"
)
cursor = conn.cursor(dictionary=True)

# ----------------- CLASSE PRINCIPAL -----------------
class BibliotecaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Biblioteca")
        self.geometry("900x600")
        self.resizable(False, False)

        # Usuários logados
        self.logged_user_id = None
        self.logged_funcionario_id = None
        self.logged_leitor_id = None
        self.logged_user_type = None

        # Frame principal
        self.main_frame = ctk.CTkFrame(self, width=860, height=560, corner_radius=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Tela inicial
        self.show_welcome()

    # ----------------- LIMPAR FRAME -----------------
    def clear_frame(self):
        for w in self.main_frame.winfo_children():
            w.destroy()

    # ====================== WELCOME ======================
    def show_welcome(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Sistema Biblioteca", font=ctk.CTkFont(size=28, weight="bold")).place(relx=0.5, rely=0.12, anchor="center")
        ctk.CTkLabel(self.main_frame, text="Interface gráfica - Modo escuro", font=ctk.CTkFont(size=14)).place(relx=0.5, rely=0.18, anchor="center")

        ctk.CTkButton(self.main_frame, text="Login - Administração", width=300, height=50, command=self.show_admin_login).place(relx=0.5, rely=0.34, anchor="center")
        ctk.CTkButton(self.main_frame, text="Login - Funcionário", width=300, height=50, command=self.show_funcionario_login).place(relx=0.5, rely=0.46, anchor="center")
        ctk.CTkButton(self.main_frame, text="Cadastro - Leitor", width=300, height=50, command=self.show_leitor_cadastro).place(relx=0.5, rely=0.58, anchor="center")
        ctk.CTkButton(self.main_frame, text="Login - Leitor", width=300, height=50, command=self.show_leitor_login).place(relx=0.5, rely=0.70, anchor="center")
        ctk.CTkButton(self.main_frame, text="Encerrar", width=140, command=self.quit).place(relx=0.5, rely=0.84, anchor="center")

    # ====================== ADMIN ======================
    def show_admin_login(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Login - Administração", font=ctk.CTkFont(size=20, weight="bold")).place(relx=0.5, rely=0.12, anchor="center")

        usuario_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Usuário", width=300)
        usuario_entry.place(relx=0.35, rely=0.33, anchor="w")
        senha_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Senha", width=300, show="*")
        senha_entry.place(relx=0.35, rely=0.45, anchor="w")

        def login_adm():
            usuario = usuario_entry.get().strip()
            senha = senha_entry.get().strip()
            cursor.execute("SELECT * FROM tb_usuarios WHERE usuario=%s AND senha=%s AND tipo='admin'", (usuario, senha))
            result = cursor.fetchone()
            if result:
                self.logged_user_id = result['id']
                messagebox.showinfo("Sucesso", "Login ADM efetuado!")
                self.show_admin_dashboard()
            else:
                messagebox.showerror("Erro", "Usuário ou senha inválidos")

        ctk.CTkButton(self.main_frame, text="Entrar", command=login_adm).place(relx=0.5, rely=0.6, anchor="center")
        ctk.CTkButton(self.main_frame, text="Voltar", fg_color="gray30", command=self.show_welcome).place(relx=0.5, rely=0.72, anchor="center")

    def show_admin_dashboard(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Admin Dashboard", font=ctk.CTkFont(size=24, weight="bold")).place(relx=0.5, rely=0.1, anchor="center")

        nome_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome", width=300)
        nome_entry.place(relx=0.35, rely=0.25, anchor="w")
        usuario_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Usuário", width=300)
        usuario_entry.place(relx=0.35, rely=0.33, anchor="w")
        senha_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Senha", width=300, show="*")
        senha_entry.place(relx=0.35, rely=0.41, anchor="w")

        def cadastrar_funcionario():
            nome = nome_entry.get().strip()
            usuario = usuario_entry.get().strip()
            senha = senha_entry.get().strip()
            if not nome or not usuario or not senha:
                messagebox.showerror("Erro", "Preencha todos os campos")
                return
            cursor.execute("INSERT INTO tb_usuarios (nome, usuario, senha, tipo) VALUES (%s,%s,%s,'funcionario')", (nome, usuario, senha))
            conn.commit()
            messagebox.showinfo("Sucesso", "Funcionário cadastrado!")

        ctk.CTkButton(self.main_frame, text="Cadastrar Funcionário", command=cadastrar_funcionario).place(relx=0.5, rely=0.55, anchor="center")
        ctk.CTkButton(self.main_frame, text="Voltar", fg_color="gray30", command=self.show_welcome).place(relx=0.5, rely=0.65, anchor="center")

    # ====================== FUNCIONÁRIO ======================
    def show_funcionario_login(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Login - Funcionário", font=ctk.CTkFont(size=20, weight="bold")).place(relx=0.5, rely=0.12, anchor="center")

        usuario_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Usuário", width=300)
        usuario_entry.place(relx=0.35, rely=0.33, anchor="w")
        senha_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Senha", width=300, show="*")
        senha_entry.place(relx=0.35, rely=0.45, anchor="w")

        def login_func():
            usuario = usuario_entry.get().strip()
            senha = senha_entry.get().strip()
            cursor.execute("SELECT * FROM tb_usuarios WHERE usuario=%s AND senha=%s AND tipo='funcionario'", (usuario, senha))
            result = cursor.fetchone()
            if result:
                self.logged_funcionario_id = result['id']
                messagebox.showinfo("Sucesso", "Login Funcionário efetuado!")
                self.show_funcionario_dashboard()
            else:
                messagebox.showerror("Erro", "Usuário ou senha inválidos")

        ctk.CTkButton(self.main_frame, text="Entrar", command=login_func).place(relx=0.5, rely=0.6, anchor="center")
        ctk.CTkButton(self.main_frame, text="Voltar", fg_color="gray30", command=self.show_welcome).place(relx=0.5, rely=0.72, anchor="center")

    def show_funcionario_dashboard(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Funcionário Dashboard", font=ctk.CTkFont(size=24, weight="bold")).place(relx=0.5, rely=0.1, anchor="center")

        ctk.CTkButton(self.main_frame, text="Registrar Empréstimo", width=300, command=self.show_registrar_emprestimo).place(relx=0.5, rely=0.3, anchor="center")
        ctk.CTkButton(self.main_frame, text="Registrar Devolução", width=300, command=self.show_registrar_devolucao).place(relx=0.5, rely=0.42, anchor="center")
        ctk.CTkButton(self.main_frame, text="Voltar", width=200, fg_color="gray30", command=self.show_welcome).place(relx=0.5, rely=0.6, anchor="center")

    # ====================== LEITOR ======================
    def show_leitor_cadastro(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Cadastro - Leitor", font=ctk.CTkFont(size=20, weight="bold")).place(relx=0.5, rely=0.12, anchor="center")

        nome_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome", width=300)
        nome_entry.place(relx=0.35, rely=0.3, anchor="w")
        cpf_entry = ctk.CTkEntry(self.main_frame, placeholder_text="CPF", width=300)
        cpf_entry.place(relx=0.35, rely=0.38, anchor="w")
        nascimento_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Data de Nascimento (YYYY-MM-DD)", width=300)
        nascimento_entry.place(relx=0.35, rely=0.46, anchor="w")
        email_entry = ctk.CTkEntry(self.main_frame, placeholder_text="E-mail", width=300)
        email_entry.place(relx=0.35, rely=0.54, anchor="w")
        telefone_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Telefone", width=300)
        telefone_entry.place(relx=0.35, rely=0.62, anchor="w")

        def cadastrar_leitor():
            nome = nome_entry.get().strip()
            cpf = cpf_entry.get().strip()
            nascimento = nascimento_entry.get().strip()
            email = email_entry.get().strip()
            telefone = telefone_entry.get().strip()

            if not nome or not cpf:
                messagebox.showerror("Erro", "Nome e CPF são obrigatórios")
                return

            cursor.execute(
                "INSERT INTO tb_leitores (nome, cpf, data_nascimento, email, telefone) VALUES (%s,%s,%s,%s,%s)",
                (nome, cpf, nascimento, email, telefone)
            )
            conn.commit()
            messagebox.showinfo("Sucesso", "Leitor cadastrado!")
            self.show_welcome()

        ctk.CTkButton(self.main_frame, text="Cadastrar", command=cadastrar_leitor).place(relx=0.5, rely=0.7, anchor="center")
        ctk.CTkButton(self.main_frame, text="Voltar", fg_color="gray30", command=self.show_welcome).place(relx=0.5, rely=0.8, anchor="center")

    def show_leitor_login(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Login - Leitor", font=ctk.CTkFont(size=20, weight="bold")).place(relx=0.5, rely=0.12, anchor="center")

        cpf_entry = ctk.CTkEntry(self.main_frame, placeholder_text="CPF", width=300)
        cpf_entry.place(relx=0.35, rely=0.33, anchor="w")
        nome_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome", width=300)
        nome_entry.place(relx=0.35, rely=0.41, anchor="w")

        def login_leitor():
            cpf = cpf_entry.get().strip()
            nome = nome_entry.get().strip()
            cursor.execute("SELECT * FROM tb_leitores WHERE cpf=%s AND nome=%s", (cpf, nome))
            result = cursor.fetchone()
            if result:
                self.logged_leitor_id = result['id']
                messagebox.showinfo("Sucesso", "Login Leitor efetuado!")
                self.show_leitor_dashboard()
            else:
                messagebox.showerror("Erro", "CPF ou Nome inválidos")

        ctk.CTkButton(self.main_frame, text="Entrar", command=login_leitor).place(relx=0.5, rely=0.55, anchor="center")
        ctk.CTkButton(self.main_frame, text="Voltar", fg_color="gray30", command=self.show_welcome).place(relx=0.5, rely=0.65, anchor="center")

    def show_leitor_dashboard(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Ficha do Leitor", font=ctk.CTkFont(size=24, weight="bold")).place(relx=0.5, rely=0.1, anchor="center")

        # Buscar empréstimos do leitor
        cursor.execute("""
            SELECT e.id, l.titulo, e.data_emprestimo, e.devolvido
            FROM tb_emprestimos e
            JOIN tb_livros l ON e.id_livro = l.id
            WHERE e.id_leitor = %s
            ORDER BY e.devolvido, e.data_emprestimo DESC
        """, (self.logged_leitor_id,))
        emprestimos = cursor.fetchall()

        if not emprestimos:
            ctk.CTkLabel(self.main_frame, text="Nenhum empréstimo encontrado.", font=ctk.CTkFont(size=14)).place(relx=0.5, rely=0.3, anchor="center")
        else:
            y_pos = 0.25
            for e in emprestimos:
                status = "Devolvido" if e['devolvido'] else "Ativo"
                texto = f"{e['titulo']} - {e['data_emprestimo'].strftime('%d/%m/%Y')} - {status}"
                ctk.CTkLabel(self.main_frame, text=texto, font=ctk.CTkFont(size=14)).place(relx=0.5, rely=y_pos, anchor="center")
                y_pos += 0.06

        ctk.CTkButton(self.main_frame, text="Sair", width=200, fg_color="gray30", command=self.show_welcome).place(relx=0.5, rely=0.85, anchor="center")

    # ====================== EMPRÉSTIMOS ======================
    def show_registrar_emprestimo(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Registrar Empréstimo", font=ctk.CTkFont(size=20, weight="bold")).place(relx=0.5, rely=0.1, anchor="center")

        # Leitores
        cursor.execute("SELECT id, nome FROM tb_leitores")
        leitores = cursor.fetchall()
        leitor_dict = {f"{l['nome']} (ID:{l['id']})": l['id'] for l in leitores}

        # Livros disponíveis
        cursor.execute("SELECT id, titulo, quantidade FROM tb_livros WHERE quantidade > 0")
        livros = cursor.fetchall()
        livro_dict = {f"{l['titulo']} (Qtd:{l['quantidade']})": l['id'] for l in livros}

        leitor_var = ctk.StringVar()
        ctk.CTkLabel(self.main_frame, text="Selecionar Leitor:").place(relx=0.3, rely=0.25, anchor="w")
        leitor_dropdown = ctk.CTkComboBox(self.main_frame, values=list(leitor_dict.keys()), variable=leitor_var, width=300)
        leitor_dropdown.place(relx=0.3, rely=0.3, anchor="w")

        livro_var = ctk.StringVar()
        ctk.CTkLabel(self.main_frame, text="Selecionar Livro:").place(relx=0.3, rely=0.37, anchor="w")
        livro_dropdown = ctk.CTkComboBox(self.main_frame, values=list(livro_dict.keys()), variable=livro_var, width=300)
        livro_dropdown.place(relx=0.3, rely=0.42, anchor="w")

        def registrar():
            leitor_id = leitor_dict.get(leitor_var.get())
            livro_id = livro_dict.get(livro_var.get())
            if not leitor_id or not livro_id:
                messagebox.showerror("Erro", "Selecione leitor e livro")
                return
            cursor.execute(
                "INSERT INTO tb_emprestimos (id_livro, id_leitor, id_funcionario, data_emprestimo, devolvido) VALUES (%s,%s,%s,NOW(),0)",
                (livro_id, leitor_id, self.logged_funcionario_id)
            )
            cursor.execute("UPDATE tb_livros SET quantidade = quantidade - 1 WHERE id = %s", (livro_id,))
            conn.commit()
            messagebox.showinfo("Sucesso", "Empréstimo registrado!")
            self.show_funcionario_dashboard()

        ctk.CTkButton(self.main_frame, text="Registrar Empréstimo", command=registrar).place(relx=0.5, rely=0.55, anchor="center")
        ctk.CTkButton(self.main_frame, text="Voltar", fg_color="gray30", command=self.show_funcionario_dashboard).place(relx=0.5, rely=0.65, anchor="center")

    # ====================== DEVOLUÇÕES ======================
    def show_registrar_devolucao(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Registrar Devolução", font=ctk.CTkFont(size=20, weight="bold")).place(relx=0.5, rely=0.1, anchor="center")

        cursor.execute("""
            SELECT e.id, l.titulo, le.nome 
            FROM tb_emprestimos e 
            JOIN tb_livros l ON e.id_livro=l.id 
            JOIN tb_leitores le ON e.id_leitor=le.id 
            WHERE e.devolvido=0
        """)
        emprestimos = cursor.fetchall()
        emp_dict = {f"{r['titulo']} - {r['nome']} (ID:{r['id']})": r['id'] for r in emprestimos}

        emp_var = ctk.StringVar()
        ctk.CTkLabel(self.main_frame, text="Selecionar Empréstimo:").place(relx=0.3, rely=0.25, anchor="w")
        emp_dropdown = ctk.CTkComboBox(self.main_frame, values=list(emp_dict.keys()), variable=emp_var, width=400)
        emp_dropdown.place(relx=0.3, rely=0.3, anchor="w")

        def registrar_devolucao():
            emp_id = emp_dict.get(emp_var.get())
            if not emp_id:
                messagebox.showerror("Erro", "Selecione um empréstimo")
                return
            cursor.execute("UPDATE tb_emprestimos SET devolvido=1 WHERE id=%s", (emp_id,))
            cursor.execute("UPDATE tb_livros l JOIN tb_emprestimos e ON l.id=e.id_livro SET l.quantidade=l.quantidade+1 WHERE e.id=%s", (emp_id,))
            conn.commit()
            messagebox.showinfo("Sucesso", "Devolução registrada!")
            self.show_funcionario_dashboard()

        ctk.CTkButton(self.main_frame, text="Registrar Devolução", command=registrar_devolucao).place(relx=0.5, rely=0.55, anchor="center")
        ctk.CTkButton(self.main_frame, text="Voltar", fg_color="gray30", command=self.show_funcionario_dashboard).place(relx=0.5, rely=0.65, anchor="center")


# ----------------- RODAR APP -----------------
if __name__ == "__main__":
    app = BibliotecaApp()
    app.mainloop()
