import email
from unicodedata import name
from urllib import response
from xml.dom.minidom import Element
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time
import re

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path='C:\Users\cpfld\OneDrive\MyDocument\GitHub\tsrAutoDownloader\chromedriver.exe')

#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disavle-dev-shm-usage')
driver = webdriver.Chrome()

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub(' ', str(data))

def get_crawl(URL):
    response = driver.get(URL)
    html = driver.page_source
    soup7 = BeautifulSoup(html, 'html.parser')
    ex_id_divs=soup7.find('div', {'id': 'view_content'})
    crawl_data = remove_html_tags(ex_id_divs)
    return crawl_data

driver.get('https://www.thesimsresource.com/account/login')
login_x_path = '/html/body/div[5]/div[1]/div/form/div[2]/p[4]/button'

driver.find_element(By.NAME,'email').send_keys('TSXmadbaby') #user ID
driver.find_element(By.NAME,'password').send_keys('HCf$dj!?!2hX29d') #user PASSWORD
driver.find_element(By.CSS_SELECTOR,"body > div.wrapper.group > div.login-box > div > form > div.login-box.auth > p:nth-child(5) > button").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#showcase-game')))
driver.get('https://www.thesimsresource.com/downloads/browse/category/sims4-objects/')

list = driver.find_elements(By.CLASS_NAME,"item-image")

for i in range(len(list)):
    print("list:",list[i])
    list[i].click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,'#big-image > div.big-info.group > div.big-info-details > div.big-download-buttons > a.okletsdothis.dl.subonly').click()

# driver.find_element(By.CSS_SELECTOR,"#nav-wrap > ul > li:nth-child(1) > a").click()
# driver.find_element(By.CSS_SELECTOR,"#nav-wrap > ul > li:nth-child(1) > div > div.download-nav > ul > li.sims4-nav-menu.sims-selected > div > ul > li:nth-child(14) > a").click()

