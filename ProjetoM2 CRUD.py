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

def confirmar_edicao_usuario():
    cpf = entry_cpf.get().strip()
    nome = entry_nome.get().strip()
    telefone = entry_telefone.get().strip()
    email = entry_email.get().strip()
    id_propriedade_usuario = entry_idpropriedade.get().strip()

    if not cpf:
        messagebox.showwarning("Atenção", "Digite o CPF para atualizar o usuário.")
        return

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        sql_usuario = """
            UPDATE usuario
            SET nome=%s, telefone=%s, email=%s, idpropriedade=%s
            WHERE cpf=%s
        """
        cursor.execute(sql_usuario, (nome, telefone, email, id_propriedade_usuario, cpf))
        conexao.commit()

        messagebox.showinfo("Sucesso", "Dados do usuário atualizados com sucesso!")

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao atualizar usuário: {erro}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

def confirmar_edicao_propriedade():


    id_propriedade = entry_id_propriedade.get().strip()
    endereco = entry_endereco.get().strip()
    bairro = entry_bairro.get().strip()
    valor = entry_valor.get().strip()
    tamanho = entry_tamanho.get().strip()
    ano_compra = entry_ano_compra.get().strip()

    if not id_propriedade:
        messagebox.showwarning("Atenção", "Digite o ID da propriedade para atualizar.")
        return

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        sql_propriedade = """
            UPDATE propriedade
            SET endereco=%s, bairro=%s, valor=%s, tamanho=%s, anocompra=%s
            WHERE id=%s
        """
        cursor.execute(sql_propriedade, (endereco, bairro, valor, tamanho, ano_compra, id_propriedade))
        conexao.commit()

        messagebox.showinfo("Sucesso", "Dados da propriedade atualizados com sucesso!")

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao atualizar propriedade: {erro}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


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


    selected_item = grid_propriedade.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione uma propriedade para editar")
        return
    
    propriedade_id = grid_propriedade.item(selected_item)["values"][0]
    
    endereco = entry7.get()
    bairro = entry8.get()
    valor = entry9.get()
    tamanho = entry10.get()
    ano_compra = entry11.get()

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        # Atualiza propriedade com base no ID
        sql = ("UPDATE propriedade SET endereco=%s, bairro=%s, valor=%s, tamanho=%s, anocompra=%s "
               "WHERE id=%s")
        valores = (endereco, bairro, valor, tamanho, ano_compra, propriedade_id)
        cursor.execute(sql, valores)
        conexao.commit()

        messagebox.showinfo("Sucesso", "Propriedade atualizada com sucesso!")
        exibir_dados()

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao editar a propriedade: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


    
    selected_item = grid_propriedade.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione uma propriedade para excluir")
        return
    
    propriedade_id = grid_propriedade.item(selected_item)["values"][0]

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        sql = "DELETE FROM propriedade WHERE id=%s"
        cursor.execute(sql, (propriedade_id,))
        conexao.commit()

        messagebox.showinfo("Sucesso", "Propriedade excluída com sucesso!")
        exibir_dados()

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao excluir a propriedade: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


    selected = grid_usuario.selection()
    if not selected:
        messagebox.showwarning("Aviso", "Selecione um usuário para editar")
        return
    values = grid_usuario.item(selected)["values"]
    cpf, nome, telefone, email, idpropriedade = values

    # Muda para aba Editar
    notebook.select(aba_editar)

# Função para carregar dados do usuário ao inserir CPF
def carregar_dados_usuario(event=None):
    cpf = entry_cpf.get().strip()
    if not cpf:
        limpar_campos_usuario()
        return
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, telefone, email, idpropriedade FROM usuario WHERE cpf = %s", (cpf,))
        resultado = cursor.fetchone()
        if resultado:
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, resultado[0])
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, resultado[1])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, resultado[2])
            entry_idpropriedade.delete(0, tk.END)
            entry_idpropriedade.insert(0, resultado[3])
        else:
            limpar_campos_usuario()
            messagebox.showinfo("Info", "Usuário não encontrado.")
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao buscar dados do usuário: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_idpropriedade.delete(0, tk.END)

# Função para carregar dados da propriedade ao inserir ID
def carregar_dados_propriedade(event=None):
    id_prop = entry_id_propriedade.get().strip()
    if not id_prop:
        limpar_campos_propriedade()
        return
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT endereco, bairro, valor, tamanho, anocompra FROM propriedade WHERE id = %s", (id_prop,))
        resultado = cursor.fetchone()
        if resultado:
            entry_endereco.delete(0, tk.END)
            entry_endereco.insert(0, resultado[0])
            entry_bairro.delete(0, tk.END)
            entry_bairro.insert(0, resultado[1])
            entry_valor.delete(0, tk.END)
            entry_valor.insert(0, resultado[2])
            entry_tamanho.delete(0, tk.END)
            entry_tamanho.insert(0, resultado[3])
            entry_ano_compra.delete(0, tk.END)
            entry_ano_compra.insert(0, resultado[4])
        else:
            limpar_campos_propriedade()
            messagebox.showinfo("Info", "Propriedade não encontrada.")
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao buscar dados da propriedade: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para limpar campos da propriedade
def limpar_campos_propriedade():
    entry_endereco.delete(0, tk.END)
    entry_bairro.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_tamanho.delete(0, tk.END)
    entry_ano_compra.delete(0, tk.END)

# Função para excluir usuário e propriedade com base no CPF e ID
def confirmar_exclusao():
    cpf = entry_excluir_cpf.get().strip()

    if not cpf:
        messagebox.showwarning("Atenção", "Digite pelo menos o CPF.")
        return

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistemaimobiliario",
        )
        cursor = conexao.cursor()

        if cpf:
            cursor.execute("DELETE FROM usuario WHERE cpf = %s", (cpf,))
        
        
        conexao.commit()
        messagebox.showinfo("Sucesso", "Dados excluídos com sucesso!")

        # Limpar campos
        entry_excluir_cpf.delete(0, tk.END)    

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao excluir dados: {erro}")

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


# Criar aba de edição no notebook (coloque após criar notebook e as outras abas)
aba_editar = ttk.Frame(notebook)
notebook.add(aba_editar, text="Editar")

# Labels e campos para Usuário
tk.Label(aba_editar, text="CPF:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_cpf = ttk.Entry(aba_editar)
entry_cpf.grid(row=0, column=1, padx=5, pady=5)
entry_cpf.bind("<FocusOut>", carregar_dados_usuario)
entry_cpf.bind("<Return>", carregar_dados_usuario)

tk.Label(aba_editar, text="Nome:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_nome = ttk.Entry(aba_editar)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

tk.Label(aba_editar, text="Telefone:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_telefone = ttk.Entry(aba_editar)
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

tk.Label(aba_editar, text="Email:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_email = ttk.Entry(aba_editar)
entry_email.grid(row=3, column=1, padx=5, pady=5)

tk.Label(aba_editar, text="ID Propriedade:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_idpropriedade = ttk.Entry(aba_editar)
entry_idpropriedade.grid(row=4, column=1, padx=5, pady=5)


# Labels e campos para Propriedade
tk.Label(aba_editar, text="ID Propriedade:").grid(row=0, column=2, sticky="e", padx=5, pady=5)
entry_id_propriedade = ttk.Entry(aba_editar)
entry_id_propriedade.grid(row=0, column=3, padx=5, pady=5)
entry_id_propriedade.bind("<FocusOut>", carregar_dados_propriedade)
entry_id_propriedade.bind("<Return>", carregar_dados_propriedade)

tk.Label(aba_editar, text="Endereço:").grid(row=1, column=2, sticky="e", padx=5, pady=5)
entry_endereco = ttk.Entry(aba_editar)
entry_endereco.grid(row=1, column=3, padx=5, pady=5)

tk.Label(aba_editar, text="Bairro:").grid(row=2, column=2, sticky="e", padx=5, pady=5)
entry_bairro = ttk.Entry(aba_editar)
entry_bairro.grid(row=2, column=3, padx=5, pady=5)

tk.Label(aba_editar, text="Valor:").grid(row=3, column=2, sticky="e", padx=5, pady=5)
entry_valor = ttk.Entry(aba_editar)
entry_valor.grid(row=3, column=3, padx=5, pady=5)

tk.Label(aba_editar, text="Tamanho:").grid(row=4, column=2, sticky="e", padx=5, pady=5)
entry_tamanho = ttk.Entry(aba_editar)
entry_tamanho.grid(row=4, column=3, padx=5, pady=5)

tk.Label(aba_editar, text="Ano de Compra:").grid(row=5, column=2, sticky="e", padx=5, pady=5)
entry_ano_compra = ttk.Entry(aba_editar)
entry_ano_compra.grid(row=5, column=3, padx=5, pady=5)

# Aba de exclusão
aba_excluir = ttk.Frame(notebook)
notebook.add(aba_excluir, text="Excluir Dados")

# Rótulos e campos de entrada
tk.Label(aba_excluir, text="CPF do Usuário:", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10)
entry_excluir_cpf = tk.Entry(aba_excluir, font=("Arial", 10))
entry_excluir_cpf.grid(row=0, column=1, padx=10, pady=10)

btn_confirmar_exclusao = tk.Button(aba_excluir, text="Confirmar Exclusão", font=("Arial", 10), command=confirmar_exclusao)
btn_confirmar_exclusao.grid(row=2, column=0, columnspan=2, pady=20)


# Botão para confirmar edição
btn_confirmar_edicao = ttk.Button(aba_editar, text="Editar Usuário", command=confirmar_edicao_usuario)
btn_confirmar_edicao.grid(row=12, column=0, columnspan=2, pady=15)

btn_confirmar_edicao = ttk.Button(aba_editar, text="Editar Propriedade", command=confirmar_edicao_propriedade)
btn_confirmar_edicao.grid(row=12, column=3, columnspan=2, pady=15)


form.mainloop()
