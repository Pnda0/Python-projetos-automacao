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

time.sleep(5)

pesquisar_grupo_click = telegram.find_element('xpath', '//*[@id="telegram-search-input"]').click()
time.sleep(3)

pesquisar_grupo = telegram.find_element('xpath', '//*[@id="telegram-search-input"]').send_keys('FIFA EV+' + Keys.ENTER)
time.sleep(3)   

click_grupo = telegram.find_element('xpath', '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/img').click()
time.sleep(3)



comparacaoClass = ''

while True: 
    ComparacaoAgora = telegram.find_elements('class name', 'text-content with-meta')[-1]
    ComparacaoAgora_text = ComparacaoAgora.text
    print(ComparacaoAgora_text)

    if comparacaoClass != ComparacaoAgora:
        print('Mensagem mais recente possível')
    else:
        comparacaoClass = ComparacaoAgora
        print('continuo com uma msg antiga')
        


