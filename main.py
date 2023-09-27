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

    })


def extract_string_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    return browser.find_element("xpath", xpath).text

def extract_numeric_from_xpath(xpath: str, browser: webdriver.Chrome) -> float:
    percentage_text = browser.find_element_by_xpath(xpath).text
    percentage_text = percentage_text.replace(',', '.')  # Replace comma with dot for decimals
    percentage_text = percentage_text.rstrip('%')  # Remove the percentage sign from the end
    return float(f'{percentage_text}%')

    return percentage_text + '%'  # Add the percentage sign back


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

def main():
    #valor = input('Digite qual empresa deseja pesquisar')
    empresa = input('Digite o codigo da empresa: ')
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
    search_bar.send_keys(empresa)
    search_bar.submit()

      # Espere 5 segundos (pode ajustar conforme necessário)

    first_result = browser.find_element('xpath', '//*[@id="results"]/div/div[2]/div[1]/div/div/a/div/div[1]/img')
    wait.until(EC.visibility_of(first_result))
    first_result.click()

    time.sleep(5)

    #Nome da Empresa
    xpath_company_name = '//*[@id="header_action"]/div[1]/div[2]/h2'
    company_name = extract_string_from_xpath(xpath_company_name, browser)
    
    #Cotação
    xpathprice = '//*[@id="cards-ticker"]/div[1]/div[2]/div/span'
    price = extract_numeric_from_xpath(xpathprice, browser)
    
    #Receita Liquida
    xpath_receita_liquida = '//*[@id="table-balance-results"]/tbody/tr[2]/td[2]/div[1]'
    receita_liquida = extract_numeric_from_xpath(xpath_receita_liquida, browser)

    #EBITA
    xpath_ebita = '//*[@id="table-balance-results"]/tbody/tr[7]/td[2]/div[1]'
    ebita = extract_numeric_from_xpath(xpath_ebita, browser)

    #EBIT
    xpath_ebit = '//*[@id="table-balance-results"]/tbody/tr[6]/td[2]/div[1]'
    ebit = extract_numeric_from_xpath(xpath_ebit, browser)

    #imposto
    xpath_tax = '//*[@id="table-balance-results"]/tbody/tr[8]/td[2]/div[1]'
    tax = extract_numeric_from_xpath(xpath_tax, browser)

    #divida bruta
    xpath_gross_debt = '//*[@id="table-balance-results"]/tbody/tr[9]/td[2]/div[1]'
    gross_debt = extract_numeric_from_xpath(xpath_gross_debt, browser)

    #Divida Liquida
    xpath_divida_liquida = '//*[@id="table-balance-results"]/tbody/tr[10]/td[2]/div[1]'
    divida_liquida = extract_numeric_from_xpath(xpath_divida_liquida, browser)
    
    #Lucro liquido
    xpath_net_revenue = '//*[@id="table-balance-results"]/tbody/tr[5]/td[2]/div[1]'
    net_revenue = extract_numeric_from_xpath(xpath_net_revenue, browser)

    #Lucro Bruto
    xpath_gross_profit = '//*[@id="table-balance-results"]/tbody/tr[4]/td[2]/div[1]'
    gross_profit = extract_numeric_from_xpath(xpath_gross_profit, browser)

    #Custo
    xpath_cost = '//*[@id="table-balance-results"]/tbody/tr[3]/td[2]/div[1]'
    cost = extract_numeric_from_xpath(xpath_cost, browser)

    #margem bruta
    xpath_gross_margin = '//*[@id="table-balance-results"]/tbody/tr[11]/td[2]'
    gross_margin = extract_numeric_from_xpath(xpath_gross_margin, browser)

    #margem ebita
    xpath_ebit_margin = '//*//*[@id="table-balance-results"]/tbody/tr[12]/td[2]'
    ebit_margin = extract_numeric_from_xpath(xpath_ebit_margin, browser)

    #margem liquida
    xpath_net_margin = '//*[@id="table-balance-results"]/tbody/tr[13]/td[2]'
    net_margin = extract_numeric_from_xpath(xpath_net_margin, browser)
    
    #ROE
    xpath_roe = '//*[@id="table-balance-results"]/tbody/tr[14]/td[2]'
    roe = extract_numeric_from_xpath(xpath_roe, browser)

    #roic
    xpath_roic = '//*[@id="table-balance-results"]/tbody/tr[15]/td[2]'
    roic = extract_numeric_from_xpath(xpath_roic, browser)



    data.loc[len(data)] = {\

                           'Empresa': company_name, 'Cotação': price,  \
                           'Divida Liquida': divida_liquida, 'Custos': cost, \
                           'Lucro Bruto': gross_profit, 'Margem Bruta': gross_margin, \
                           'Margem Ebita': ebit_margin, 'Margem Liquida': net_margin, \
                           'Divida Bruta': gross_debt,  'ROE': roe, 'Receita Liquida': receita_liquida, \
                           'EBITA': ebita, 'EBIT': ebit, 'Impostos': tax, \
                           'Margem EBITA': ebit_margin, 'Lucro Liquido': net_revenue, 'Roic': roic                      
                                                    
 }

    print(data)

    data.to_csv('dados.csv', sep=';', encoding='utf-8')

    loaded_data = pd.read_csv('dados.csv', sep=';', encoding='utf-8')

    print(loaded_data)
  
    browser.quit()

if __name__ == "__main__":
    main()
