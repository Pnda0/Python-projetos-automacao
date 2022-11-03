from cgitb import text
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from imap_tools import MailBox, AND
from email.mime.base import MIMEBase
from email import encoders

# DADOS

data_ini = '19/10'
data_fim = '30/10'

email_from = 'seu email'
email_password = 'sua senha'
email_smtp_server = 'smtp.office365.com'

# Destino
destination = ['email do destino']

# Assunto
subject = 'Assunto'



# Formatar cabeçalho do e-mail
msg = MIMEMultipart()
msg['From'] = email_from
msg['Subject'] = subject

# Corpo do e-mail
text = f'''Corpo do e-mail'''

# Habilitando formato HTML
msg_text = MIMEText(text, 'html')

# Anexando a mensagem
msg.attach(msg_text)

# Anexando Planilha
anexo = r'C:\Users\Padrao\Downloads\excel.xlsx'
attachment = open(anexo, 'rb')

att = MIMEBase('aplication', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition',f'attachment; filename=dfpronto22.xlsx')
attachment.close()
msg.attach(att)


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





