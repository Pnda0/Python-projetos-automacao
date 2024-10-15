import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Informações do remetente e do destinatário
email_de = "seu_email@gmail.com"
email_para = "destinatario_email@gmail.com"
senha = "sua_senha"

# Criação da mensagem
assunto = "Assunto do E-mail"
corpo = "Olá, esta é uma mensagem simples enviada por Python."

# Configuração da mensagem MIME
msg = MIMEMultipart()
msg['From'] = email_de
msg['To'] = email_para
msg['Subject'] = assunto

# Anexar o corpo do e-mail
msg.attach(MIMEText(corpo, 'plain'))

# Configuração do servidor SMTP
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Encriptar a conexão
    server.login(email_de, senha)

    # Envio da mensagem
    texto = msg.as_string()
    server.sendmail(email_de, email_para, texto)

    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o e-mail: {e}")
finally:
    server.quit()
