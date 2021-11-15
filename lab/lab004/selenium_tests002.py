from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--headless')

service = Service('lab/lab004/chromedriver.exe')
driver = webdriver.Chrome(service = service)

driver.get('https://www.fizyka.pw.edu.pl/index.php/Pracownicy/Lista-pracownikow/Pracownicy-badawczo-dydaktyczni')

elements = driver.find_elements(By.CSS_SELECTOR, 'h2, h2 + div')
for element in elements:
    print(element.text)

#time.sleep(5)
driver.close()
