import requests
import os



# Acesso ao grupo e Robo
#token = 'seu Token'
#chat_id = 'seu id' 
token = '5786749554:AAEPWln5TR4cQfie8G8YC5y20qvTk_md-Nc'
chat_id = '-610286523' 
message = 'Fala ai brow'

url = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}')


# enviando a mensagem
req = requests.post(url)
print(req)

