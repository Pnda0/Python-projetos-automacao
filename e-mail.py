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
msg['To'] = 'emaildoremetente@hotmail.com'
# Corpo do e-mail
text = f'''Corpo do e-mail'''

# Habilitando formato HTML
msg_text = MIMEText(text, 'html')

# Anexando a mensagem
msg.attach(msg_text)

# Abrindo Planilha em excel
anexo = r'C:\Users\Padrao\Downloads\excel.xlsx'
attachment = open(anexo, 'rb')

# Lendo planilha em encode 64
att = MIMEBase('aplication', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

# Adicionando um cabeçalho ao anexo
att.add_header('Content-Disposition',f'attachment; filename=dfpronto22.xlsx')
attachment.close()
# Anexando de fato
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
    smtp.sendmail(email_from, msg['To'], msg.as_string())

    # Encerrar conexão
    smtp.quit()
    print('E-mail enviado!')
except Exception as erro:
    print(f'Falha ao enviar e-mail:{erro}')





