from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
import datetime

def extract_date_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    date = browser.find_element("xpath", xpath) \
        .text.replace('/', '')
    return int(re.sub("[^\\d]", "", date))

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
cnpj = 60872504000123
browser.get('https://cnpj.linkana.com/')
search_bar = browser.find_element("xpath", '//*[@id="app"]/div/main/div/div[1]/div/div[2]/form/div/input')
wait.until(EC.visibility_of(search_bar))
search_bar.send_keys(cnpj)
time.sleep(1)
search_bar.submit()
time.sleep(1)
click_in_company_name = browser.find_element('xpath', '//*[@id="app"]/div/main/div/div/a/div/div[1]/p[1]')
click_in_company_name.click()
time.sleep(1)
xpath_data_abertura = '//*[@id="app"]/div/main/div[2]/ul[1]/li[5]/p'
data_abertura = extract_date_from_xpath(xpath_data_abertura, browser)
data_str = str(data_abertura)
data_abertura = data_str[-4:]











print(data_abertura)