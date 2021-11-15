from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = Options()
options.add_argument('--disable-notifications')

service = Service('lab/lab004/chromedriver.exe')
driver = webdriver.Chrome(service = service, options = options)

driver.get('https://www.reddit.com/r/ChuckNorris/')

# button = driver.find_element(By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div[1]/section/div/section/section/form[2]/button')
# button.click()

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div[1]/section/div/section/section/form[2]/button')))
button.click()

# ActionChains

for i in range(10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
