from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
import datetime

def create_question() -> pd.DataFrame:
    return pd.DataFrame({
        'DÍVIDA LÍQUIDA - LUCRO LÍQUIDO': [], #feito
        'DIVIDENDOS': [],	#feito
        'Crescimento de receitas lucro >5% ultimos 5 anos': [], 
        'P/VP abaixo de 5': [], #feito
        'Líquida/EBITDA é menor que 2': [], #feito
        '+30 anos de mercado? (Fundação)': [], #feito
        'P/L < 30': [], #feito
        'livre de controle ESTATAL ou concentração em cliente único?': [],
        'LUCRO OPERACIONAL>0': [], #feito
        'pesquisa e inovação?': [],
        'Tem uma boa gestão?': [],
        'É líder nacional ou mundial': [],
        'BLUE CHIP?': [],
        'PERENIDADE O setor em que atua +100 anos?': [],     
        
    })

def create_data_frame() -> pd.DataFrame:
    return pd.DataFrame({
        'Empresa': [],
        'Cotação': [],
        'Divida Liquida': [],
        'Custos': [],
        'Lucro Liquido': [],
        'Lucro Bruto': [],
        'Margem Bruta': [],
        'Margem Liquida': [],
        'Divida Bruta': [],
        'Divida Liquida': [],
        'Roic': [],
        'ROE': [],
        'Receita Liquida': [],
        'EBITA': [],
        'EBIT': [],
        'Impostos': [],
        'Margem EBITA': [],
        'Dy': [],
        'P/VP': [],
        'P/L': [],

    })


def extract_string_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    return browser.find_element("xpath", xpath).text

def extract_cnpj_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    value = browser.find_element("xpath", xpath) \
        .text.replace('.', '')
    return float(re.sub("[^\\d]", "", value))

def extract_date_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    date = browser.find_element("xpath", xpath) \
        .text.replace('/', '')
    return int(re.sub("[^\\d]", "", date))


def extract_numeric_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    value = browser.find_element("xpath", xpath) \
        .text.replace(',', '.')

    scale = None
    if 'Bilhões' in value:
        scale = 1000000000

    elif 'Milhões' in value:
        scale = 1000000

    elif 'Mil' in value:
        scale = 1000

    if '%' in value:
        percentage_text = value.rstrip('%')  # Remove the percentage sign from the end
        return float(percentage_text)
    if '-' == value:
        return float(0)

    if scale:
        return float(re.sub("[^\\d.-]", "", value)) * scale

    return float(re.sub("[^\\d.-]", "", value))
