from stonks_analytics.data_handler.pandas_handler import PandasHandler


class QuestionFiiHandler(PandasHandler):
    columns = [
        "Fundo",
        "Dy_maior8",
        "pvp_menor1.2",
        "Liq.dia_maior1M",
        "Vacancia_menor10",
        "Prazo_indet",
        "Valor_Patrim_maior500M",
        "Dy_5anos_maior7",
        "Pontuação",

    ]

    def __init__(self, file_path="csv/questionfii.csv"):
        super().__init__(file_path)

    def append(self, question: dict):
        if question["Fundo"] in self.loaded_data["Fundo"].unique():
            self.loaded_data.loc[self.loaded_data["Fundo"] == question["Fundo"]] = [
                question[column] if column in question else None
                for column in self.columns
            ]

        else:
            self.loaded_data.loc[len(self.loaded_data)] = question

    def get_question_from_company(self, fundo: str):
        return self.loaded_data.loc[
            self.loaded_data["Fundo"] == fundo
        ].to_dict("records")[0]
