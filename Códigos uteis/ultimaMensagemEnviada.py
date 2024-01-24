import requests
import urllib.request
import json





token = 'seu token'
chat_id = 'chat_id' 

# Constrói a URL da API do Telegram para obter as últimas atualizações
url = f"https://api.telegram.org/bot{token}/getUpdates?chat_id={chat_id}"

# Envia a solicitação HTTP GET para a API do Telegram
response = requests.get(url)

# Analisa a resposta JSON da API do Telegram para obter a última mensagem enviada
result = response.json()["result"][-1]
last_message = result["message"]["text"]

# Imprime a última mensagem
print(last_message)

