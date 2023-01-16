import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium import webdriver
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime

# Acesso ao grupo e Robo
token = '5360566736:AAEJ2xv0eOPJMYtE23aimJM96LGFW90x8Ws'
chat_id = -837533517 

url = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}')

messages = []

# Mensagem enviada
for update in url.getUpdates():
    if update.message and update.message.chat.id == chat_id:
        messages.append(update.message)

# Formatando o envio das mensagens

# Now you have a list of messages from the group
for message in messages:
    print(message.text)



