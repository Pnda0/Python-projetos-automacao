from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
telegram = webdriver.Chrome(service=service)


# Navega para a página web do Telegram
telegram.get("https://web.telegram.org/")
telegram.maximize_window()

# espera o usuário fazer o login manualmente
input('Faça o login no Telegram Web e pressione Enter para continuar...')

time.sleep(3)

telegram.find_element('xpath', '//*[@id="telegram-search-input"]').send_keys('FIFA EV+' + Keys.ENTER)
time.sleep(3)

telegram.find_element('xpath', '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/h3').click()
time.sleep(4)

messages = telegram.find_element('xpath', '//div[@class="im_history_message_wrap"]') # encontrar todas as mensagens atuais
print(messages)


# encontrar e clicar no link desejado
for message in messages:
    text = message.text
    if 'link_desejado' in text: # substitua por um texto que apareça no link que deseja clicar
        link = message.find_element_by_xpath('//a')
        link.click()
        break # sair do loop após clicar no link
