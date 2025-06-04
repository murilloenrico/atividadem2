# Chatbot Híbrido - Gemini + Manual

import customtkinter
from CTkMessagebox import CTkMessagebox
from datetime import datetime
import google.generativeai as genai
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download("punkt", quiet=True)

# Configurar API do Gemini
genai.configure(api_key="AIzaSyBP3weQmItN4JTZ-mwBpa5debjyKQXznxo")  # Troque pela sua API real
modelo = genai.GenerativeModel('gemini-1.5-flash')
chat = modelo.start_chat(history=[])

# Dicionário de respostas manuais
respostaspersonalizadas = {
    "propriedade": "Para cadastrar, preencha ID, endereço, bairro, valor, tamanho e ano de compra.",
    "usuario": "Informe nome, CPF, telefone, email e o ID da propriedade vinculada.",
    "cpf": "Deve ser único. Usado para identificar o usuário.",
    "cadastro": "Preencha os campos corretamente e clique no botão de cadastrar.",
    "erro": "Erro comum: CPF ou ID já cadastrado, ou campo vazio.",
    "editar": "Digite o CPF do usuário e os novos dados, depois confirme.",
    "exibir": "Exibe os dados cadastrados nas tabelas da interface.",
    "limpar": "Os campos são limpos automaticamente após o cadastro.",
}

stemmer = PorterStemmer()

# Função do chatbot
def chatbot(mensagem):
    try:
        palavras = word_tokenize(mensagem.lower())
        palavra_raiz = [stemmer.stem(p) for p in palavras]
        
        for palavra in palavra_raiz:
            if palavra in respostaspersonalizadas:
                return respostaspersonalizadas[palavra]
        
        # Se não encontrou manualmente, usar Gemini
        resposta_gemini = chat.send_message(mensagem)
        return resposta_gemini.text

    except Exception as e:
        return f"Ocorreu um erro ao processar a mensagem: {e}"

# Função para processar entrada
def enviar_mensagem():
    mensagem_usuario = entrada_usuario.get()
    if not mensagem_usuario.strip():
        return

    resposta_chatbot = chatbot(mensagem_usuario)
    caixa_texto.insert(customtkinter.END, f"\n{label_id.cget('text')}: {mensagem_usuario}\n", "usuario")
    caixa_texto.insert(customtkinter.END, f"Chatbot-AI: {resposta_chatbot}\n", "chatbot")
    entrada_usuario.delete(0, customtkinter.END)

# ----------------------------------
# Interface com customtkinter
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")

janela = customtkinter.CTk()
janela.title("Chatbot")
janela.geometry("460x580")
janela.resizable(False, False)

# Caixa de texto
caixa_texto = customtkinter.CTkTextbox(janela, wrap=customtkinter.WORD, height=500, width=440)
caixa_texto.pack()
caixa_texto.tag_config("usuario", foreground="cyan", justify="left")
caixa_texto.tag_config("chatbot", foreground="white", justify="left")

# Nome do usuário
dialog = customtkinter.CTkInputDialog(text="Entre com seu nome:", title="Identificação")
nome = dialog.get_input()
if nome is None or nome.strip() == "":
    nome = "Você"

# Exibir saudação inicial
data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
caixa_texto.insert(customtkinter.END, f"[{data_hora}]\nChatbot-AI: Olá, {nome}! Como posso te ajudar hoje?\n", "chatbot")

# Moldura inferior
frame_entrada = customtkinter.CTkFrame(janela)
frame_entrada.pack(pady=5)

# Label nome
label_id = customtkinter.CTkLabel(frame_entrada, text=nome + ":", font=("Helvetica", 12, "bold"))
label_id.grid(row=0, column=0, padx=5)

# Entrada do usuário
entrada_usuario = customtkinter.CTkEntry(frame_entrada, width=220, font=("Helvetica", 12))
entrada_usuario.grid(row=0, column=1, padx=5)

# Botão enviar
botao_enviar = customtkinter.CTkButton(frame_entrada, text="Enviar", command=enviar_mensagem)
botao_enviar.grid(row=0, column=2, padx=5)

janela.mainloop()
