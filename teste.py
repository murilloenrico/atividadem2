import mysql.connector
from tkinter import Tk, ttk
import tkinter as tk
from tkinter import messagebox

# Função para inserir a propriedade no banco de dados
def inserir_propriedade():
    id_propriedade = entry6.get()  # ID da propriedade inserido pelo usuário
    endereco = entry7.get()
    bairro = entry8.get()
    valor = entry9.get()
    tamanho = entry10.get()
    ano_compra = entry11.get()  # Ano de compra como número inteiro

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        # Comando SQL para Inserir a propriedade
        sql = f"INSERT INTO propriedade(id, endereco, bairro, valor, tamanho, anocompra) VALUES ({id_propriedade}, '{endereco}', '{bairro}', {valor}, '{tamanho}', {ano_compra})"
        cursor.execute(sql)
        conexao.commit()  # Confirma no banco o insert

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Cadastro de Propriedade inserido com sucesso! ID da Propriedade: {id_propriedade}")
        
        # Limpar campos de entrada de propriedade
        entry6.delete(0, tk.END)
        entry7.delete(0, tk.END)
        entry8.delete(0, tk.END)
        entry9.delete(0, tk.END)
        entry10.delete(0, tk.END)
        entry11.delete(0, tk.END)

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro: {erro}")

    finally:
        # Fechar a conexão
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para inserir o usuário no banco de dados
def inserir_usuario():
    nome = entry1.get()
    cpf = entry2.get()
    telefone = entry4.get()
    email = entry5.get()
    idpropriedade = entry12.get()  # O ID da Propriedade inserido pelo usuário (relacionado à chave estrangeira)

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        # Comando SQL para Inserir o usuário
        sql = f"INSERT INTO usuario(cpf, nome, telefone, email, idpropriedade) VALUES ({cpf}, '{nome}', '{telefone}', '{email}', {idpropriedade})"
        cursor.execute(sql)
        conexao.commit()  # Confirma no banco o insert

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Cadastro de Usuário inserido com sucesso!")
        
        # Limpar campos de entrada de usuário
        limpar_campos_usuario()

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro: {erro}")

    finally:
        # Fechar a conexão
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para limpar campos de entrada do usuário
def limpar_campos_usuario():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry12.delete(0, tk.END)

# Função para exibir os dados na aba de dados
def exibir_dados():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        # Consultar dados de usuários e propriedades
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()

        cursor.execute("SELECT * FROM propriedade")
        propriedades = cursor.fetchall()

        # Limpar o grid
        for item in grid_usuario.get_children():
            grid_usuario.delete(item)
        for item in grid_propriedade.get_children():
            grid_propriedade.delete(item)

        # Inserir dados na árvore (grid) de usuários
        for usuario in usuarios:
            grid_usuario.insert("", "end", values=usuario)

        # Inserir dados na árvore (grid) de propriedades
        for propriedade in propriedades:
            grid_propriedade.insert("", "end", values=propriedade)

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao carregar dados: {erro}")
    finally:
        # Fechar a conexão
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para editar usuário
def editar_usuario():
    selected_item = grid_usuario.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione um usuário para editar")
        return
    
    usuario_id = grid_usuario.item(selected_item)["values"][0]
    
    nome = entry1.get()
    cpf = entry2.get()
    telefone = entry4.get()
    email = entry5.get()
    idpropriedade = entry12.get()

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        # Comando SQL para editar o usuário
        sql = f"UPDATE usuario SET nome='{nome}', telefone='{telefone}', email='{email}', idpropriedade={idpropriedade} WHERE cpf={cpf}"
        cursor.execute(sql)
        conexao.commit()  # Confirma no banco o update

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")

        # Atualizar os dados na interface
        exibir_dados()

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao editar o usuário: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para excluir usuário
def excluir_usuario():
    selected_item = grid_usuario.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione um usuário para excluir")
        return
    
    usuario_id = grid_usuario.item(selected_item)["values"][0]
    cpf = grid_usuario.item(selected_item)["values"][1]

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        # Comando SQL para excluir o usuário
        sql = f"DELETE FROM usuario WHERE cpf={cpf}"
        cursor.execute(sql)
        conexao.commit()  # Confirma no banco o delete

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")

        # Atualizar os dados na interface
        exibir_dados()

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao excluir o usuário: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Criar a janela principal
form = Tk()
form.title("Sistema Imobiliário")
form.geometry("950x650")
form.configure(background="white")

# Estilo do ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", font=("Arial", 10), padding=5)
style.configure("TEntry", font=("Arial", 10))

# Criar o notebook (abas)
notebook = ttk.Notebook(form)
notebook.pack(fill="both", expand=True)

# Aba de cadastro
aba_cadastro = ttk.Frame(notebook)
notebook.add(aba_cadastro, text="Cadastro")

# Aba de dados
aba_dados = ttk.Frame(notebook)
notebook.add(aba_dados, text="Exibir Dados")

# -- Cadastro de Propriedade --
# Rótulos e campos de entrada para o formulário de Propriedade
label6 = tk.Label(aba_cadastro, text="ID da Propriedade: ", font=("Arial", 10))
label6.grid(row=0, column=0, padx=10, pady=10)
entry6 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry6.grid(row=0, column=1, padx=10, pady=10)

label7 = tk.Label(aba_cadastro, text="Endereço da Propriedade: ", font=("Arial", 10))
label7.grid(row=1, column=0, padx=10, pady=10)
entry7 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry7.grid(row=1, column=1, padx=10, pady=10)

label8 = tk.Label(aba_cadastro, text="Bairro: ", font=("Arial", 10))
label8.grid(row=2, column=0, padx=10, pady=10)
entry8 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry8.grid(row=2, column=1, padx=10, pady=10)

label9 = tk.Label(aba_cadastro, text="Valor: ", font=("Arial", 10))
label9.grid(row=3, column=0, padx=10, pady=10)
entry9 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry9.grid(row=3, column=1, padx=10, pady=10)

label10 = tk.Label(aba_cadastro, text="Tamanho: ", font=("Arial", 10))
label10.grid(row=4, column=0, padx=10, pady=10)
entry10 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry10.grid(row=4, column=1, padx=10, pady=10)

label11 = tk.Label(aba_cadastro, text="Ano de Compra: ", font=("Arial", 10))
label11.grid(row=5, column=0, padx=10, pady=10)
entry11 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry11.grid(row=5, column=1, padx=10, pady=10)

btn_inserir_propriedade = tk.Button(aba_cadastro, text="Cadastrar Propriedade", command=inserir_propriedade)
btn_inserir_propriedade.grid(row=6, column=1, columnspan=2, pady=20)

# -- Cadastro de Usuário --
label1 = tk.Label(aba_cadastro, text="Nome: ", font=("Arial", 10))
label1.grid(row=7, column=0, padx=10, pady=10)
entry1 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry1.grid(row=7, column=1, padx=10, pady=10)

label2 = tk.Label(aba_cadastro, text="CPF: ", font=("Arial", 10))
label2.grid(row=8, column=0, padx=10, pady=10)
entry2 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry2.grid(row=8, column=1, padx=10, pady=10)

label4 = tk.Label(aba_cadastro, text="Telefone: ", font=("Arial", 10))
label4.grid(row=9, column=0, padx=10, pady=10)
entry4 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry4.grid(row=9, column=1, padx=10, pady=10)

label5 = tk.Label(aba_cadastro, text="Email: ", font=("Arial", 10))
label5.grid(row=10, column=0, padx=10, pady=10)
entry5 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry5.grid(row=10, column=1, padx=10, pady=10)

label12 = tk.Label(aba_cadastro, text="ID Propriedade: ", font=("Arial", 10))
label12.grid(row=11, column=0, padx=10, pady=10)
entry12 = tk.Entry(aba_cadastro, font=("Arial", 10))
entry12.grid(row=11, column=1, padx=10, pady=10)

btn_inserir_usuario = tk.Button(aba_cadastro, text="Cadastrar Usuário", command=inserir_usuario)
btn_inserir_usuario.grid(row=12, column=1, columnspan=2, pady=20)

# -- Exibição de Dados --
grid_usuario = ttk.Treeview(aba_dados, columns=("CPF", "Nome", "Telefone", "Email", "ID Propriedade"))
grid_usuario.heading("#1", text="CPF")
grid_usuario.heading("#2", text="Nome")
grid_usuario.heading("#3", text="Telefone")
grid_usuario.heading("#4", text="Email")
grid_usuario.heading("#5", text="ID Propriedade")
grid_usuario.pack(fill="both", expand=True)

grid_propriedade = ttk.Treeview(aba_dados, columns=("ID", "Endereço", "Bairro", "Valor", "Tamanho", "Ano de Compra"))
grid_propriedade.heading("#1", text="ID")
grid_propriedade.heading("#2", text="Endereço")
grid_propriedade.heading("#3", text="Bairro")
grid_propriedade.heading("#4", text="Valor")
grid_propriedade.heading("#5", text="Tamanho")
grid_propriedade.heading("#6", text="Ano de Compra")
grid_propriedade.pack(fill="both", expand=True)

btn_exibir_dados = tk.Button(aba_dados, text="Exibir Dados", command=exibir_dados, font=("Arial", 10))
btn_exibir_dados.pack(pady=20)

# Adicionando botões de Editar e Excluir
btn_editar_usuario = tk.Button(aba_dados, text="Editar Usuário", command=editar_usuario, font=("Arial", 10))
btn_editar_usuario.pack(pady=10)

btn_excluir_usuario = tk.Button(aba_dados, text="Excluir Usuário", command=excluir_usuario, font=("Arial", 10))
btn_excluir_usuario.pack(pady=10)

form.mainloop()
