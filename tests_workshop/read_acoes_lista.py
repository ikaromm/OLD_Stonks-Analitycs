import pandas as pd

tabela = pd.read_csv("acoeslista.csv", sep=",", encoding="utf-8")

tickers = []


for acao in tabela["Código"]:
    # Verifique se o item atual termina com "4"
    if acao.endswith("4"):
        # Verifique se já existe um item na lista filtrada que termina com "3"
        if any(item.endswith("3") for item in tabela["Código"]):
            # Se sim, não adicione o item atual à lista filtrada
            continue
    tickers.append(acao)

print(tickers)

# for codigo in tabela['Código']:
#     tickers.append(codigo)

print(len(tickers))

# for tick in tickers:
#     print(tickers)
