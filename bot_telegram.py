import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium import webdriver
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime
import tkinter as tk 

#criando a janelas
janela = tk.Tk()
janela.title("Esteira AD")
janela.geometry("250x150")

#criando as variáveis
login_input = tk.StringVar()
senha_input = tk.StringVar()

#criando as labels
login_label = tk.Label(janela, text = "Login:")
login_label.place(x = 10, y = 10)

senha_label = tk.Label(janela, text = "Senha:")
senha_label.place(x = 10, y = 40)

#criando os campos de entrada
login_entry = tk.Entry(janela, textvariable = login_input)
login_entry.place(x = 70, y = 10, width = 150)

senha_entry = tk.Entry(janela, textvariable = senha_input, show = "*")
senha_entry.place(x = 70, y = 50, width = 150)

#função para verificar login e senha
def verificar():
    login_verif = "Esteira.ad"
    senha_verif = "Venus"
    if login_entry.get() == login_verif and senha_entry.get() == senha_verif:
        janela.destroy()
    else:
        tk.messagebox.showerror("Senha incorreta", "A senha ou usuário estão incorretos. Por favor, tente novamente.")

#criando o botão 
botao = tk.Button(janela, text = "Entrar", command = verificar)
botao.place(x = 80, y = 90, width = 80)

janela.mainloop()


# Acesso ao grupo e Robo
<<<<<<< HEAD
token = 'seu Token'
chat_id = 'seu id' 
=======
token = '5360566736:AAEJ2xv0eOPJMYtE23aimJM96LGFW90x8Ws'
chat_id = '-837533517' 
>>>>>>> d69f5cbf12f9b7a2fb43925c8675fc22da21ad90

url = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}/sendMessage')

messages = ['Fala ai brow']

# enviando a mensagem
req = requests.post(url)
print(req)

