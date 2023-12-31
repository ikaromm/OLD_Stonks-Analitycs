import pandas as pd

# Leia o arquivo CSV
tabela = pd.read_csv("csv/datasql.csv", sep=";", encoding="utf-8")
tabelafii = pd.read_csv("csv/datafiitratada.csv", sep=";", encoding="utf-8")


#Crie uma lista de índices das linhas que não atendem ao requisito
indices_para_remover = tabela.index[tabela["Soma_Total"] < 8].tolist()
indices_para_remover1 = tabelafii.index[tabelafii["Pontuação"] <= 5].tolist()

# Use o método drop para remover as linhas com base nos índices
tabela = tabela.drop(indices_para_remover)
tabelafii = tabelafii.drop(indices_para_remover1)

# Reset os índices do DataFrame após a remoção das linhas
tabela.reset_index(drop=True, inplace=True)
tabelafii.reset_index(drop=True, inplace=True)

# Imprima o DataFrame resultante
print(tabela[:50])
print(tabela[50:])

print(tabelafii)
