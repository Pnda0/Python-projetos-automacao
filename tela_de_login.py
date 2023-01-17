import tkinter as tk 

#criando a janela
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")

#criando as variáveis
login_input = tk.StringVar()
senha_input = tk.StringVar()

#criando as labels
login_label = tk.Label(janela, text = "Login:")
login_label.place(x = 20, y = 10)

senha_label = tk.Label(janela, text = "Senha:")
senha_label.place(x = 20, y = 50)

#criando os campos de entrada
login_entry = tk.Entry(janela, textvariable = login_input)
login_entry.place(x = 70, y = 10, width = 200)

senha_entry = tk.Entry(janela, textvariable = senha_input, show = "*")
senha_entry.place(x = 70, y = 50, width = 200)

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
botao.place(x = 120, y = 80, width = 80)

janela.mainloop()