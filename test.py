import pandas as pd

# Create a DataFrame
df = pd.read_csv("acoeslista.csv", sep=",", encoding="utf-8")
df = df["Código"]
df = df.to_csv("tickers_acoes.csv", sep=";", encoding="utf-8", index=False)