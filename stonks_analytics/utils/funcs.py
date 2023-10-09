from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import random

# from bardapi import Bard
from dotenv import load_dotenv


import os
import datetime
import time
import re


def get_api_key() -> dict:
    load_dotenv()

    api_key = os.environ.get("BARD_API_KEY")

    if api_key is None:
        raise Exception("API key not found")

    return {"token": api_key}


def sum_of_variables() -> int:
    return (
        div_liq_men_luc_liq
        + divdends
        + pvp_less_5
        + liq_ebta
        + pl_less_30
        + more_than_30y
        + luc_op
    )


def bard_answer(answer: str) -> int:
    if answer == "não":
        return 0
    else:
        return 1


def extract_string_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    return browser.find_element("xpath", xpath).text


def extract_cnpj_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    value = browser.find_element("xpath", xpath).text.replace(".", "")
    return float(re.sub("[^\\d]", "", value))


def extract_date_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    try:
        date = browser.find_element("xpath", xpath).text.replace("/", "")
        return int(re.sub("[^\\d]", "", date))
    except:
        return 0


def extract_numeric_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    value = browser.find_element("xpath", xpath).text.replace(".", "").replace(",", ".")

    scale = None

    if "Bilhões" in value or "B" in value:
        scale = 1000000000

    elif "Milhões" in value or "M" in value:
        scale = 1000000

    elif "Mil" in value:
        scale = 1000

    elif "K" in value:
        scale = 1000    

    if "%" in value:
        percentage_text = value.rstrip("%")  # Remove the percentage sign from the end
        return float(percentage_text)
    if "-" == value:
        return float(0)

    if scale:
        return float(re.sub("[^\\d.-]", "", value)) * scale

    return float(re.sub("[^\\d.-]", "", value))


def set_chrome_options():
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    return chrome_options


def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1
