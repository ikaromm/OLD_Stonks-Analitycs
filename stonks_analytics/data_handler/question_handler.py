from stonks_analytics.data_handler.pandas_handler import PandasHandler


class QuestionHandler(PandasHandler):
    columns = [
        "Company Name",
        "DÍVIDA LÍQUIDA - LUCRO LÍQUIDO",
        "DIVIDENDOS",
        "LUCRO OPERACIONAL>0",
        "P/VP abaixo de 5",
        "Líquida/EBITDA é menor que 2",
        "+30 anos de mercado? (Fundação)",
        "P/L < 30",
        "Crescimento de receitas lucro >5perc ultimos 5 anos",
        "Soma_total",
    ]

    def __init__(self, file_path="csv/question.csv"):
        super().__init__(file_path)

    def append(self, question: dict):
        if question["Company Name"] in self.loaded_data["Company Name"].unique():
            self.loaded_data.loc[
                self.loaded_data["Company Name"] == question["Company Name"]
            ] = [ question[column] if column in question else None for column in self.columns ]

        else:
            self.loaded_data.loc[len(self.loaded_data)] = question

    def get_question_from_company(self, company_name: str):
        return self.loaded_data.loc[
            self.loaded_data["Company Name"] == company_name
        ].to_dict("records")[0]
