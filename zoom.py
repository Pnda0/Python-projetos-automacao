from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https:www.youtube.com.br')
time.sleep(3)
driver.execute_script("document.body.style.zoom='50%'")
time.sleep(999)
