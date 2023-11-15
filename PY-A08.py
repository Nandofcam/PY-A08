# Importação do módulo
from tkinter import *
from tkinter import messagebox

janela = Tk()

# Título da janela
janela.title("Sistema de Cadastro")

# Tamanho e posicionamento da janela
# (larguraxaltura+horizontal+vertical)
janela.geometry("320x80+550+250")

#Função para enviar o nome
def enviar():
    # Receber o valor da entrada
    nome = campo_nome.get()
    # Caixa de mensagem
    messagebox.showinfo("Boas vindas!",
                        f"Bem vindo, {nome}.")

# Caixa de entrada
# Entrada
campo_nome = Entry(janela, font="Calibri 16 normal")

# Campo para digitar
label_nome = Label(janela, text="Nome:", fg="green",
                   font="Calibri 16 bold")

# Botão de enviar
button_enviar = Button(janela, text="Enviar",
                       fg="white", font="Arial 16 bold",
                       bg="green", command=enviar)

# Elementos da janela
label_nome.grid(row=0, column=0)
button_enviar.grid(row=1, column=0)
campo_nome.grid(row=0, column=1)

janela.mainloop()