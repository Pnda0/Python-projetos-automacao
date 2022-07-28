import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium import webdriver
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime

# Acesso ao grupo e Robo
token = 'Sua chave token'
chat_id = 'Seu chat ID'

# Mensagem enviada
mensagem = f"""Texto enviado com sucesso! ✅"""

# Formatando o envio das mensagens
url = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={mensagem}')

# Requisição 
reposta = requests.get(url)
print(reposta.json())




