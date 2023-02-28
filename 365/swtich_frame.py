from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
janela = webdriver.Chrome(service=service)

service = Service(ChromeDriverManager().install())
bet = webdriver.Chrome(service=service)

janela.get('https://www.youtube.com/watch?v=f7Goh4LpHdM&t=2075s')
time.sleep(8)

token_janela_atual = janela.current_window_handle
print(token_janela_atual)

id_janelas = janela.window_handles
print(id_janelas)

janela.switch_to.window(
    janela.window_handles[-1]
)


time.sleep(999)