from stonks_analytics.data_handler import (
    DataHandler,
    QuestionHandler,
    DataSqlHandler,
    FiiTratado,
    DataFiiHandler,
    QuestionFiiHandler,
)
from stonks_analytics.utils.funcs import *
from stonks_analytics.utils.config import *


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd

# from bardapi import Bard
# from dotenv import load_dotenv

import datetime
import time
import re
import os
import random


def main():
    escolha = input("Deseja rodar para [F]IIS ou [A]ÇOES? ").upper()

    if escolha == "A":
        tabela = pd.read_csv("acoeslista.csv", sep=",", encoding="utf-8")  ##ação
    elif escolha == "F":
        tabela = pd.read_csv("fiilista.csv", sep=",", encoding="utf-8")  ##FII
    else:
        print("Opção inválida")
        return

    tickers = []

    if escolha == "A":
        for acao in tabela["Código"]:
            if acao.endswith("4"):
                if any(item.endswith("3") for item in tabela["Código"]):
                    continue

            tickers.append(acao)
    ###### storage all tickers

    elif escolha == "F":
        for fii in tabela["FUNDOS"]:
            tickers.append(fii)

    for item in tickers:
        unique_sequence = uniqueid()
        empresa = item

        if escolha == "A":
            data = DataHandler()
            data.load_data()

            question = QuestionHandler()
            question.load_data()

            dadosql = DataSqlHandler()
            dadosql.load_data()

        elif escolha == "F":
            data = DataFiiHandler()
            data.load_data()

            question = QuestionFiiHandler()
            question.load_data()

            datatrat = FiiTratado()
            datatrat.load_data()

        
        # empresa = input("Digite o codigo da empresa: ")

        browser = webdriver.Chrome(options=set_chrome_options())
        wait = WebDriverWait(browser, 10)

        browser.get("https://investidor10.com.br")

        search_bar = browser.find_element(
            "xpath",
            "/html/body/div[3]/div/div/section[1]/div/div/div[1]/div/form/div/span/input[2]",
        )
        wait.until(EC.visibility_of(search_bar))
        search_bar.send_keys(empresa)
        search_bar.submit()

        try:
            first_result = browser.find_element(
                "xpath", '//*[@id="results"]/div/div[2]/div[1]/div/div/a/div/div[1]/img'
            )
            wait.until(EC.visibility_of(first_result))
            first_result.click()

            time.sleep(1)

        except:
            print("Nenhum resultado encontrado")
            browser.quit()
            continue

        if escolha == "A":
            xpath_company_name = '//*[@id="header_action"]/div[1]/div[2]/h2'
            pl_element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath_company_name))
            )
            company_name = extract_string_from_xpath(xpath_company_name, browser)

            # Cotação
            xpathprice = '//*[@id="cards-ticker"]/div[1]/div[2]/div/span'
            pl_element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpathprice))
            )
            price = extract_numeric_from_xpath(xpathprice, browser)
            price1 = extract_numeric_from_xpath(xpathprice, browser)
            print(price)
            # Receita Liquida
            xpath_receita_liquida = (
                '//*[@id="table-balance-results"]/tbody/tr[2]/td[2]/div[1]'
            )
            pl_element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath_receita_liquida))
            )
            receita_liquida = extract_numeric_from_xpath(xpath_receita_liquida, browser)

            # EBITA
            xpath_ebita = '//*[@id="table-balance-results"]/tbody/tr[7]/td[2]/div[1]'
            ebita = extract_numeric_from_xpath(xpath_ebita, browser)

            # EBIT
            xpath_ebit = '//*[@id="table-balance-results"]/tbody/tr[6]/td[2]/div[1]'
            ebit = extract_numeric_from_xpath(xpath_ebit, browser)

            # imposto
            xpath_tax = '//*[@id="table-balance-results"]/tbody/tr[8]/td[2]/div[1]'
            tax = extract_numeric_from_xpath(xpath_tax, browser)

            # divida bruta
            xpath_gross_debt = (
                '//*[@id="table-balance-results"]/tbody/tr[9]/td[2]/div[1]'
            )
            gross_debt = extract_numeric_from_xpath(xpath_gross_debt, browser)

            # Divida Liquida
            xpath_divida_liquida = (
                '//*[@id="table-balance-results"]/tbody/tr[10]/td[2]/div[1]'
            )
            divida_liquida = extract_numeric_from_xpath(xpath_divida_liquida, browser)

            # Lucro liquido
            xpath_net_revenue = (
                '//*[@id="table-balance-results"]/tbody/tr[5]/td[2]/div[1]'
            )
            net_revenue = extract_numeric_from_xpath(xpath_net_revenue, browser)

            # Lucro Bruto
            xpath_gross_profit = (
                '//*[@id="table-balance-results"]/tbody/tr[4]/td[2]/div[1]'
            )
            gross_profit = extract_numeric_from_xpath(xpath_gross_profit, browser)

            # Custo
            xpath_cost = '//*[@id="table-balance-results"]/tbody/tr[3]/td[2]/div[1]'
            cost = extract_numeric_from_xpath(xpath_cost, browser)

            # margem bruta
            xpath_gross_margin = '//*[@id="table-balance-results"]/tbody/tr[11]/td[2]'
            gross_margin = extract_numeric_from_xpath(xpath_gross_margin, browser)

            # margem ebita
            xpath_ebit_margin = '//*//*[@id="table-balance-results"]/tbody/tr[12]/td[2]'
            ebit_margin = extract_numeric_from_xpath(xpath_ebit_margin, browser)

            # margem liquida
            xpath_net_margin = '//*[@id="table-balance-results"]/tbody/tr[13]/td[2]'
            net_margin = extract_numeric_from_xpath(xpath_net_margin, browser)

            # ROE
            xpath_roe = '//*[@id="table-balance-results"]/tbody/tr[14]/td[2]'
            roe = extract_numeric_from_xpath(xpath_roe, browser)

            # ROA
            xpath_roa = '//*[@id="table-indicators"]/div[22]/div[1]/span'
            roa = extract_numeric_from_xpath(xpath_roa, browser)

            # roic
            xpath_roic = '//*[@id="table-balance-results"]/tbody/tr[15]/td[2]'
            roic = extract_numeric_from_xpath(xpath_roic, browser)

            xpath_dy = '//*[@id="cards-ticker"]/div[5]/div[2]/span'
            dy = extract_numeric_from_xpath(xpath_dy, browser)

            xpath_pvp = '//*[@id="cards-ticker"]/div[4]/div[2]/span'
            pvp = extract_numeric_from_xpath(xpath_pvp, browser)

            xpath_growth5y = '//*[@id="checklist"]/div/div[1]/div[7]/label/span'
            growth5y = extract_numeric_from_xpath(xpath_growth5y, browser)

            xpath_pl = '//*[@id="cards-ticker"]/div[3]/div[2]/span'
            pl = extract_numeric_from_xpath(xpath_pl, browser)

            xpath_cnpj = (
                '//*[@id="data_about"]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]'
            )
            cnpj = float(extract_cnpj_from_xpath(xpath_cnpj, browser))

            xpath_fundation = (
                '//*[@id="data_about"]/div[2]/div/div[1]/table/tbody/tr[5]/td[2]'
            )
            fundation = extract_date_from_xpath(xpath_fundation, browser)

            xpath_VPA = '//*[@id="table-indicators"]/div[17]/div[1]/span'
            VPA = extract_numeric_from_xpath(xpath_VPA, browser)

            xpath_LPA = '//*[@id="table-indicators"]/div[18]/div[1]/span'
            LPA = extract_numeric_from_xpath(xpath_LPA, browser)

            try:
                xpath_setor = '//*[@id="table-indicators-company"]/div[14]/a/span[2]'
                setor = extract_string_from_xpath(xpath_setor, browser)

                xpath_segmento = '//*[@id="table-indicators-company"]/div[15]/a/span[2]'
                segmento = extract_string_from_xpath(xpath_segmento, browser)
            except:
                setor = "Não encontrado"
                segmento = "Não encontrado"

            try:
                xpath_tag_along = '//*[@id="table-indicators-company"]/div[12]/span[2]'
                tag_along = extract_numeric_from_xpath(xpath_tag_along, browser)

                xpath_freefloat = '//*[@id="table-indicators-company"]/div[11]/span[2]'
                free_float = extract_numeric_from_xpath(xpath_freefloat, browser)
            except:
                tag_along = 0
                free_float = 0

        elif escolha == "F":
            try:        
                xpath_fundo = '//*[@id="header_action"]/div[1]/div[2]/h1'
                fundo = extract_string_from_xpath(xpath_fundo, browser)
            except:
                continue

            xpath_cotacao = '//*[@id="cards-ticker"]/div[1]/div[2]/div/span'
            cotacao = extract_numeric_from_xpath(xpath_cotacao, browser)

            xpath_dy12m = '//*[@id="cards-ticker"]/div[2]/div[2]/div/span'
            dy12m = extract_numeric_from_xpath(xpath_dy12m, browser)

            xpath_pvp = '//*[@id="cards-ticker"]/div[3]/div[2]/span'
            pvp = extract_numeric_from_xpath(xpath_pvp, browser)
            try:
                xpath_liq_diaria = '//*[@id="cards-ticker"]/div[4]/div[2]/span'
                liq_diaria = extract_numeric_from_xpath(xpath_liq_diaria, browser)

            except:
                liq_diaria = 0
            try:
                xpath_valorizacao = '//*[@id="cards-ticker"]/div[5]/div[2]/div/span'
                valorizacao = extract_numeric_from_xpath(xpath_valorizacao, browser)

            except:
                valorizacao = 0

            xpath_publico = '//*[@id="table-indicators"]/div[3]/div[2]/div/span'
            publico = extract_string_from_xpath(xpath_publico, browser)

            xpath_mandato = '//*[@id="table-indicators"]/div[4]/div[2]/div/span'
            mandato = extract_string_from_xpath(xpath_mandato, browser)

            xpath_segmento = '//*[@id="table-indicators"]/div[5]/div[2]/div/span'
            segmento = extract_string_from_xpath(xpath_segmento, browser)

            xpath_tipo_fundo = '//*[@id="table-indicators"]/div[6]/div[2]/div/span'
            tipo_fundo = extract_string_from_xpath(xpath_tipo_fundo, browser)

            xpath_duracao = '//*[@id="table-indicators"]/div[7]/div[2]/div/span'
            duracao = extract_string_from_xpath(xpath_duracao, browser)

            xpath_gestao = '//*[@id="table-indicators"]/div[8]/div[2]/div/span'
            gestao = extract_string_from_xpath(xpath_gestao, browser)

            xpath_taxa_adm = '//*[@id="table-indicators"]/div[9]/div[2]/div/span'
            taxa_adm = extract_string_from_xpath(xpath_taxa_adm, browser)


            try: 
                xpath_dy5anos = '//*[@id="dividends-section"]/div[1]/div[1]/span[2]/text()'
                dy5anos = extract_numeric_from_xpath(xpath_dy5anos, browser)
            except:
                dy5anos = 0    

            try:
                xpath_vacancia = '//*[@id="table-indicators"]/div[9]/div[2]/div/span'
                vacancia = extract_numeric_from_xpath(xpath_vacancia, browser)

            except:
                vacancia = 100

            try:
                xpath_valor_patr = '//*[@id="table-indicators"]/div[14]/div[2]/div/span'
                valor_patr = extract_numeric_from_xpath(xpath_valor_patr, browser)
            
            except:
                valor_patr = 0

            try:
                xpath_ult_rend = '//*[@id="table-indicators"]/div[15]/div[2]/div/span'
                ult_rend = extract_numeric_from_xpath(xpath_ult_rend, browser)

            except:
                ult_rend = 0

            try:
                num_rows = 15

                imv_values = []

                for i in range(1, num_rows + 1):
                    xpath = (
                        f'//*[@id="properties-index-table"]/tbody/tr[{i}]/td[2]/span'
                    )
                    imv = extract_numeric_from_xpath(xpath, browser)
                    imv_values.append(imv)
            except:
                imv_values = sum(imv_values)

        browser.quit()

       

        if escolha == "A":
            data.append(
                {
                    "Empresa": company_name,
                    "Cotação": price,
                    "Divida_Liquida": divida_liquida,
                    "Custos": cost,
                    "Lucro_Bruto": gross_profit,
                    "Margem_Bruta": gross_margin,
                    "Margem_Ebita": ebit_margin,
                    "Margem_Liquida": net_margin,
                    "Divida_Bruta": gross_debt,
                    "ROE": roe,
                    "Receita_Liquida": receita_liquida,
                    "EBITA": ebita,
                    "EBIT": ebit,
                    "Impostos": tax,
                    "Margem_EBITA": ebit_margin,
                    "Lucro_Liquido": net_revenue,
                    "Roic": roic,
                    "Dy": dy,
                    "P/VP": pvp,
                    "P/L": pl,
                    "VPA": VPA,
                    "LPA": LPA,
                }
            )

            current_date = datetime.datetime.now()
            current_year = current_date.year
            existence_time = current_year - int(fundation)

            div_liq_men_luc_liq = int(
                1 if float(net_revenue) - float(divida_liquida) > 0 else 0
            )
            divdends = 1 if float(dy) > 3 else 0
            pvp_less_5 = 1 if float(pvp) < 5 else 0
            liq_ebta = 1 if (float(divida_liquida) / float(ebita)) < 2 else 0
            pl_less_10 = 1 if float(pl) < 15 else 0
            more_than_10y = 1 if float(existence_time) > 30 else 0
            luc_op = 1 if float(ebit) > 0 else 0
            graham_formula = (
                float((22.5 * float(VPA) * float(LPA)) ** (1 / 2))
                if float(VPA) > 0 and float(LPA) > 0
                else 0
            )
            roe_calc = 1 if float(roe) > 15 else 0
            roa_calc = 1 if float(roa) > 10 else 0
            roic_calc = 1 if float(roic) > 12 else 0
            tag_along_calc = 1 if float(tag_along) > 90 else 0
            free_float_calc = 1 if float(free_float) >= 50 else 0

            # Calculate the sum of the variables
            sum_of_variables = (
                div_liq_men_luc_liq
                + divdends
                + pvp_less_5
                + liq_ebta
                + pl_less_10
                + more_than_10y
                + luc_op
                + roe_calc
                + roa_calc
                + roic_calc
                + tag_along_calc
                + free_float_calc
            )

            soma_tot = int(sum_of_variables)

            # Assuming 'question' is a DataFrame, you can assign the values to it
            question.append(
                {
                    "Empresa": company_name,
                    "Div.Liq_menos_Luc.Liq": div_liq_men_luc_liq,
                    "Dividendos": divdends,
                    "PVP_menor5": pvp_less_5,
                    "Liq_sobre_Ebita_menor2": liq_ebta,
                    "PL_menor15": pl_less_10,
                    "Ano_mercado_maior10": more_than_10y,
                    "Luc.Operacional": luc_op,
                    "Roe_maior15": roe_calc,
                    "Roa_maior10": roa_calc,
                    "Roic_maior12": roic_calc,
                    "Free_float50": free_float_calc,
                    "Tag_along100": tag_along_calc,
                    "Soma_total": sum_of_variables,
                    "Formula_Graham": round(graham_formula, 2),
                    "Cotacao": round(float(price1), 2),
                }
            )

            dadosql.append(
                {
                    "ID": next(unique_sequence),
                    "Codigo": empresa,
                    "Empresa": company_name,
                    "Setor": setor,
                    "Segmento": segmento,
                    "PVP": round(float(pvp), 2),
                    "Tag_Along": tag_along,
                    "Free_Float": free_float,
                    "Graham": round(float(graham_formula), 2),
                    "Cotacao": price,
                    "Soma_Total": soma_tot,
                }
            )

            data.save_data()
            question.save_data()
            dadosql.save_data()

            num_columns = len(question.columns) - 4
            print(company_name)
            print(data.loaded_data)
            print(question.loaded_data)
            print(dadosql.loaded_data)
            print(f"A soma das perguntas é {soma_tot} e o maximo = {num_columns}")
            print(
                f"O valor pela formula graham (sqrt(22.5*VPA*LPA)) é {round(float(graham_formula),2)}"
            )
            print(
                f"Preço ação - formula graham: {round(price - float(graham_formula),2)}"
            )

        if escolha == "F":      
           
            data.append(
                {
                    "Fundo": fundo,
                    "Dy12m": dy12m,
                    "Cotação": cotacao,
                    "PVP": pvp,
                    "Liq. Diaria": liq_diaria,
                    "Valorização (12m)": valorizacao,
                    "Tipo de Fundo": tipo_fundo,
                    "Gestão": gestao,
                    "Taxa de ADM": taxa_adm,
                    "Valor Patrimonial": valor_patr,
                    "Segmento": segmento,
                    "QNT Imoveis": imv_values,
                    "Vacancia": vacancia,
                    "Prazo de Duração": duracao,
                    "Público-Alvo": publico,
                    "Mandato": mandato,
                    "Dy5anos": dy5anos,
                    "Ult. Rendimento": ult_rend,
                    
                }
            )

            dy_maior8 = 1 if dy12m > 8 else 0
            pvp_menor1_2 = 1 if pvp < 1.2 else 0
            vacancia_menor10 = 1 if vacancia < 10 else 0
            prazo_indet = 1 if duracao == "INDETERMINADO" else 0
            valor_patrim_maior500 = 1 if valor_patr > 500000000 else 0
            liq_dia_1m = 1 if liq_diaria > 1000000 else 0
            dy_5anos_maior7 = 1 if dy5anos > 7 else 0

            sum_of_variables = (
                dy_maior8
                + pvp_menor1_2
                + vacancia_menor10
                + prazo_indet
                + valor_patrim_maior500
                + liq_dia_1m
                + dy_5anos_maior7
            )

          
            
            question.append(
                {
                    "Fundo": fundo,
                    "Dy_maior8": dy_maior8,
                    "pvp_menor1.2": pvp_menor1_2,
                    "Liq.dia_maior1M": liq_dia_1m,
                    "Vacancia_menor10": vacancia_menor10,
                    "Prazo_indet": prazo_indet,
                    "Valor_Patrim_maior500M": valor_patrim_maior500,
                    "Dy_5anos_maior7": dy_5anos_maior7,
                    "Pontuação": sum_of_variables,
                }
            )

            datatrat.append(
                {
                    "Fundo": fundo,
                    "Dy12m": dy12m,
                    "Cotação": cotacao,
                    "PVP": pvp,
                    "Prazo de Duração": duracao,
                    "Taxa de ADM": taxa_adm,
                    "Vacancia": vacancia,
                    "Ult. Rendimento": ult_rend,
                    "QNT Imoveis": imv_values,
                    "Dy5anos": dy5anos,
                    "Pontuação": sum_of_variables,           

                }
            )

            data.save_data()              
            question.save_data()
            datatrat.save_data()

            print(data.loaded_data)
            print(question.loaded_data)
            print(datatrat.loaded_data)

if __name__ == "__main__":
    main()
