from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time

def getscreenshotofurl(url):
    service2 = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service2, )
    driver.get(url)
    time.sleep(2)

    element = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/div')
    width = 800
    height = element.size['height'] + 500
    driver.set_window_size(width, height)
    time.sleep(3)
    driver.save_screenshot('Captcha_BMG.png')

driver = getscreenshotofurl('https://www.bmgconsig.com.br/acompanhamento/consignacao/acompanhamentoConsignacao.jsf?novaPesquisa=true')
print('Print realizado')
time.sleep(5)

base_url = 'https://api.telegram.org/bot5360566736:AAEJ2xv0eOPJMYtE23aimJM96LGFW90x8Ws/sendPhoto'

my_file = open(r'C:\Users\Alan\Downloads\Alan\Python\AD Python\AD-Promotora\Atendimento\Captcha_BMG.png', 'rb')

parametros = {
    "chat_id" : "-837533517",
    "caption" : "Realizar captcha"
}

files = {
    "photo" : my_file
}


resp = requests.get(base_url, data=parametros, files=files)
print(resp.text)
print('Foto Enviada')
    





