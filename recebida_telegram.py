import urllib.request
import json

token = 'seu token'
chat_id = 'chat_id' 

# Constrói a URL da API do Telegram para obter as últimas atualizações
url = f"https://api.telegram.org/bot{token}/getUpdates?chat_id={chat_id}"

# Envia a solicitação HTTP GET para a API do Telegram
req = urllib.request.urlopen(url)

# Analisa a resposta JSON da API do Telegram para obter a última mensagem recebida
try:
    data = json.loads(req.read())
    last_message = data["result"][-1]["message"]["text"]
    # Imprime a última mensagem
    print(last_message)
except:
    print('Não havia mensagem')
    
