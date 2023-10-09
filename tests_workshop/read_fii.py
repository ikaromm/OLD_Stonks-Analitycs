import pandas as pd

tabela = pd.read_csv("fiilista.csv", sep=",", encoding="utf-8")
codigo = tabela["FUNDOS"].tolist() 

print(codigo, sep="\n")
