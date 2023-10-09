from stonks_analytics.data_handler.pandas_handler import PandasHandler


class DataSqlHandler(PandasHandler):
    columns = [
        "ID",
        "Codigo",
        "Empresa",
        "Setor",
        "Segmento",
        "PVP",
        "Tag_Along",
        "Free_Float",
        "Graham",
        "Cotacao",
        "Soma_Total",
    ]

    def __init__(self, file_path="csv/datasql.csv"):
        super().__init__(file_path)

    def append(self, dadosql: dict):
        if dadosql["Empresa"] in self.loaded_data["Empresa"].unique():
            self.loaded_data.loc[self.loaded_data["Empresa"] == dadosql["Empresa"]] = [
                dadosql[column] if column in dadosql else None
                for column in self.columns
            ]

        else:
            self.loaded_data.loc[len(self.loaded_data)] = dadosql

    def get_question_from_company(self, company_name: str):
        return self.loaded_data.loc[
            self.loaded_data["Empresa"] == company_name
        ].to_dict("records")[0]
