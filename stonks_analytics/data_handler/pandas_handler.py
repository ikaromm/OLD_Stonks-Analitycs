import pandas as pd

from pathlib import Path


class PandasHandler:

    loaded_data: pd.DataFrame #expected value is a df

    columns: list[str] ## same

    def __init__(self, file_path=None):
        file_path = Path(file_path)

        self.validate_file_path(file_path)
        self.validate_dataframe_columns()

        self.file_path = file_path

    def validate_file_path(self, file_path: Path):
        if file_path is None:
            raise NotImplementedError("File path is required")

        if not file_path.parent.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)

    def validate_dataframe_columns(self):
        if self.columns is None:
            raise NotImplementedError("Columns is required")

        if not isinstance(self.columns, list):
            raise TypeError("Columns must be a list")

        if len(self.columns) == 0:
            raise ValueError("Columns must not be empty")

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                self.loaded_data = pd.read_csv(file, sep=";", encoding="utf-8")
        except FileNotFoundError:
            self.loaded_data = pd.DataFrame(columns=self.columns)

    def save_data(self):
        with open(self.file_path, "w") as file:
            self.loaded_data.to_csv(file, sep=";", encoding="utf-8", index=False)

    def append(self, dados: dict):
        raise NotImplementedError("Append method is not implemented")