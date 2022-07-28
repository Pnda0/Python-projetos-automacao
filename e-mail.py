from cgitb import text
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from imap_tools import MailBox, AND


# DADOS

email_from = 'seuemail.com.br'
email_password = 'senha do seu email'
email_smtp_server = 'smtp.office365.com'

# Destino
destination = ['email que voce deseja enviar uma mensagem']

# Assunto
subject = 'Novidades em breve :)'

# Formatar cabeçalho do e-mail
msg = MIMEMultipart()
msg['From'] = email_from
msg['Subject'] = subject

# Corpo do e-mail
text = '''Bom dia!
há um bom tempo que não faço vídeos, mas estou empolgado XD'''

# Habilitando formato HTML
msg_text = MIMEText(text, 'html')

# Anexando a mensagem
msg.attach(msg_text)

try:
    # Enviando
    smtp = smtplib.SMTP(email_smtp_server, 587)

    # Se identificando ao servidor

    smtp.ehlo()

    # Iniciando uma conexão segura e se identificar novamente
    smtp.starttls()
    smtp.ehlo()

    # Logando
    smtp.login(email_from, email_password)

    # Enviar 
    smtp.sendmail(email_from, ','.join(destination), msg.as_string())

    # Encerrar conexão
    smtp.quit()
    print('E-mail enviado!')
except Exception as erro:
    print(f'Falha ao enviar e-mail:{erro}')

