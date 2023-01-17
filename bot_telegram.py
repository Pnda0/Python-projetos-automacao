import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium import webdriver
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime

# Acesso ao grupo e Robo
token = 'seu Token'
chat_id = 'seu chat-id' 

url = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}')

messages = ['Escreva sua mensagem aqui']

# enviando a mensagem
req = requests.post(url)
print(req)

