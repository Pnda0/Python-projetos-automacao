from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def getscreenshotofurl(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    driver = webdriver.Chrome('E:\Python\Python\chromedriver.exe', options=chrome_options)
    driver.get(url)
    time.sleep(2)

    element = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer')
    width = 1920
    height = element.size['height'] + 1000
    driver.set_window_size(width, height)
    time.sleep(3)
    driver.save_screenshot('Printeste.png')
    driver.quit()

getscreenshotofurl('https://www.youtube.com/')


