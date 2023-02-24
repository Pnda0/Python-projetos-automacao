from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
bet = webdriver.Chrome(service=service)





string = """Usuario meNSAGEM🎮 FIFA-Canal do BrunoApostador ®🎮
            
⚽️ Votizlove vs Makcwelllm 🔼 
(Chelsea vs Barcelona)

🔥 Tip: Over Asiático 2 @1.75

🎯 Placar: 0-0 (🕒 Tempo: 02:55)

https://www.bet365.com/dl/sportsbookredirect?bet=1&bs=133492414-202597447~3/4

Resultado:

14:03:16"""

link_inicio = string.find('https://www.bet365.com/')
link_fim = string.find('\n', link_inicio)
link = string[link_inicio:link_fim]

print(link)

bet.get(link)
time.sleep(99)


