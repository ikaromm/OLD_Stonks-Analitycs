from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re


def create_data_frame() -> pd.DataFrame:
    return pd.DataFrame({
        'Empresa': [],
        'Cotação': [],
        'Divida Liquida': [],
        'Custos': [],
        'Lucro Liquido': []
    })


def extract_string_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    return browser.find_element("xpath", xpath).text


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

    if scale:
        return float(re.sub("[^\\d.-]", "", value)) * scale

    return float(re.sub("[^\\d.-]", "", value))

def main():
    #valor = input('Digite qual empresa deseja pesquisar')
    
    data = create_data_frame()

    # Abre o navegador Chrome
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    # Navega até o site da Amazon
    browser.get("https://investidor10.com.br")

    # Aguarde um tempo para a página carregar completamente

    # time.sleep(3)  # Espere 2 segundos (pode ajustar conforme necessário)

    search_bar = browser.find_element("xpath", "/html/body/div[3]/div/div/section[1]/div/div/div[1]/div/form/div/span/input[2]")
    wait.until(EC.visibility_of(search_bar))
    search_bar.send_keys('petr4')
    search_bar.submit()

      # Espere 5 segundos (pode ajustar conforme necessário)

    first_result = browser.find_element('xpath', '//*[@id="results"]/div/div[2]/div[1]/div/div/a/div/div[1]/img')
    wait.until(EC.visibility_of(first_result))
    first_result.click()

    time.sleep(3)

    #Nome da Empresa
    xpath_company_name = '//*[@id="header_action"]/div[1]/div[2]/h2'
    company_name = extract_string_from_xpath(xpath_company_name, browser)
    
    #Cotação
    xpathprice = '//*[@id="cards-ticker"]/div[1]/div[2]/div/span'
    price = extract_numeric_from_xpath(xpathprice, browser)
    
    #Divida Liquida
    xpath_divida_liquida = '//*[@id="table-balance-results"]/tbody/tr[10]/td[2]/div[1]'
    divida_liquida = extract_numeric_from_xpath(xpath_divida_liquida, browser)
    
    #Lucro liquido
    xpath_net_revenue = '//*[@id="table-balance-results"]/tbody/tr[5]/td[2]/div[1]'
    net_revenue = extract_numeric_from_xpath(xpath_net_revenue, browser)

    #Custo
    xpath_cost = '//*[@id="table-balance-results"]/tbody/tr[3]/td[2]/div[1]'
    cost = extract_numeric_from_xpath(xpath_cost, browser)



    data.loc[len(data)] = {'Empresa': company_name, 'Cotação': price, 'Divida Liquida': divida_liquida, 'Custos': cost, 'Lucro Liquido': net_revenue}

    print(data)

    data.to_csv('dados.csv', sep=';', encoding='utf-8')

    loaded_data = pd.read_csv('dados.csv', sep=';', encoding='utf-8')

    print(loaded_data)
  
    browser.quit()

if __name__ == "__main__":
    main()
