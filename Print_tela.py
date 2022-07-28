from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def getscreenshotofurl(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    driver = webdriver.Chrome('C:\Python\chromedriver.exe', options=chrome_options)
    driver.get(url)
    time.sleep(2)

    element = driver.find_element_by_xpath('//*[@id="cnt"]')
    width = 1920
    height = element.size['height'] + 1000
    driver.set_window_size(width, height)
    time.sleep(3)
    driver.save_screenshot('Printeste.png')
    driver.quit()

getscreenshotofurl('https://www.google.com/search?q=chrome+driver&oq=chrome&aqs=chrome.0.69i59j69i57j69i60l3j5l3.596j0j7&sourceid=chrome&ie=UTF-8')



