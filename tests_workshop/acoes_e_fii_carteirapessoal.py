import pandas as pd

# Leia o arquivo CSV
tabela = pd.read_csv("csv/datasql.csv", sep=";", encoding="utf-8")
tabelafii = pd.read_csv("csv/datafiitratada.csv", sep=";", encoding="utf-8")

#Crie uma lista de índices das linhas que não atendem ao requisito

tickers_fii= [
        "GALG11",
        "MXRF11",
        "BTCI11",
        "RECR11",
        "XPLG11",
        "ALZR11",
        "HGLG11",
        "VGIR11",
        "VISC11",
        "VGHF11",
        "BTLG11",
        "RBRF11",
        "KNSC11"

]

tickers_acao = [
    "VALE3",
    "RECEV3",
    "KEPL3",
    "CURY3",
    "VULC3",
    "LEVE3",
    "GGBR4",
    "LREN3",
    "ALSO3",
    "DIRR3",
    "MILS3",
    "RANI3",
    "CAMB3",
    "CSUD3",
    "CLSC4",
    "CMIG4",
    "ITSA4",
    "BBAS3",
    "TASA4",
    "SLCE3",
    "B3SA3",
    "PETR4",
    "SUZB3",
    "KLBN4",
  
    

]

indices_para_remover = tabelafii[~tabelafii["Fundo"].isin(tickers_fii)].index
indices_para_remover1 = tabela[~tabela["Codigo"].isin(tickers_acao)].index

# Use o método drop para remover as linhas com base nos índices
tabela = tabela.drop(indices_para_remover1)

tabelafii = tabelafii.drop(indices_para_remover)

# Reset os índices do DataFrame após a remoção das linhas
tabela.reset_index(drop=True, inplace=True)
tabelafii.reset_index(drop=True, inplace=True)

tabela.to_csv("tests_workshop/acao_carteira.csv", sep=";", encoding="utf-8", index=False)
tabelafii.to_csv("tests_workshop/fii_carteira.csv", sep=";", encoding="utf-8", index=False)


# Imprima o DataFrame resultante
print(tabela)
print()
print(tabelafii)
