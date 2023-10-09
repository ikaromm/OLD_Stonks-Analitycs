from stonks_analytics.data_handler.pandas_handler import PandasHandler


class FiiTratado(PandasHandler):
    columns = [
        "Fundo",
        "Dy12m",
        "Cotação",
        "PVP",
        "Prazo de Duração",
        "Taxa de ADM",
        "Vacancia",
        "Ult. Rendimento",
        "QNT Imoveis",
        "Dy5anos",
        "Pontuação",
    ]

    def __init__(self, file_path="csv/datafiitratada.csv"):
        super().__init__(file_path)

    def append(self, dadosql: dict):
        if dadosql["Fundo"] in self.loaded_data["Fundo"].unique():
            self.loaded_data.loc[self.loaded_data["Fundo"] == dadosql["Fundo"]] = [
                dadosql[column] if column in dadosql else None
                for column in self.columns
            ]

        else:
            self.loaded_data.loc[len(self.loaded_data)] = dadosql

    def get_question_from_company(self, fundo: str):
        return self.loaded_data.loc[
            self.loaded_data["Fundo"] == fundo
        ].to_dict("records")[0]
