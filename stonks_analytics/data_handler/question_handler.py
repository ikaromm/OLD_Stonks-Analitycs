from stonks_analytics.data_handler.pandas_handler import PandasHandler


class QuestionHandler(PandasHandler):
    columns = [

        "Empresa",
        "Div.Liq_menos_Luc.Liq",
        "Dividendos",
        "Luc.Operacional",
        "PVP_menor5",
        "Liq_sobre_Ebita_menor2",
        "Ano_mercado_maior10",
        "PL_menor10",
        "Roe_maior15",
        "Roa_maior10"
        "Roic_maior12",
        "Tag_along100",
        "Free_float50",
        "Soma_total",
        "Formula_Graham",
        "Cotacao"
    ]

    def __init__(self, file_path="csv/question.csv"):
        super().__init__(file_path)

    def append(self, question: dict):
        if question["Empresa"] in self.loaded_data["Empresa"].unique():
            self.loaded_data.loc[
                self.loaded_data["Empresa"] == question["Empresa"]
            ] = [ question[column] if column in question else None for column in self.columns ]

        else:
            self.loaded_data.loc[len(self.loaded_data)] = question

    def get_question_from_company(self, company_name: str):
        return self.loaded_data.loc[
            self.loaded_data["Empresa"] == company_name
        ].to_dict("records")[0]
