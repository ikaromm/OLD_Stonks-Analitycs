from stonks_analytics.data_handler.pandas_handler import PandasHandler


class DataHandler(PandasHandler):
    columns = [
        "Empresa",
        "Cotação",
        "Divida_Liquida",
        "Custos",
        "Lucro_Liquido",
        "Lucro_Bruto",
        "Margem_Bruta",
        "Margem_Liquida",
        "Divida_Bruta",
        "Divida_Liquida",
        "Roic",
        "ROE",
        "Receita_Liquida",
        "EBITA",
        "EBIT",
        "Impostos",
        "Margem_EBITA",
        "Dy",
        "P/VP",
        "P/L",
        "VPA",
        "LPA",
    ]

    def __init__(self, file_path="csv/data.csv"):
        super().__init__(file_path)

    def append(self, dados: dict):
        if dados["Empresa"] in self.loaded_data["Empresa"].unique():
            self.loaded_data.loc[self.loaded_data["Empresa"] == dados["Empresa"]] = [
                dados[column] for column in self.columns
            ]

        else:
            self.loaded_data.loc[len(self.loaded_data)] = dados

    def get_dados_from_empresa(self, empresa: str):
        return self.loaded_data.loc[self.loaded_data["Empresa"] == empresa].to_dict(
            "records"
        )[0]
