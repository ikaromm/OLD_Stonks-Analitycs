from stonks_analytics.data_handler.pandas_handler import PandasHandler


class DataFiiHandler(PandasHandler):
    columns = [
        "Fundo",
        "Dy12m",
        "Cotação",
        "PVP",
        "Liq. Diaria",
        "Valorização (12m)",
        "Tipo de Fundo",
        "Gestão",
        "Taxa de ADM",
        "Valor Patrimonial",
        "Segmento",
        "QNT Imoveis",
        "Vacancia",
        "Prazo de Duração",
        "Público-Alvo",
        "Mandato",
        "Ult. Rendimento",
        "Dy5anos"
    ]

    def __init__(self, file_path="csv/DataFii.csv"):
        super().__init__(file_path)

    def append(self, dados: dict):
        if dados["Fundo"] in self.loaded_data["Fundo"].unique():
            self.loaded_data.loc[self.loaded_data["Fundo"] == dados["Fundo"]] = [
                dados[column] for column in self.columns
            ]

        else:
            self.loaded_data.loc[len(self.loaded_data)] = dados

    def get_dados_from_empresa(self, fundo: str):
        return self.loaded_data.loc[self.loaded_data["Fundo"] == fundo].to_dict(
            "records"
        )[0]
