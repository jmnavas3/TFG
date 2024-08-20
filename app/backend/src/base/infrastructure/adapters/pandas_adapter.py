import pandas as pd


class PandasAdapter:
    def __init__(self, engine, csv_file: str, table_name: str):
        self._engine = engine
        self.csv_file = csv_file
        self.table_name = table_name

    def import_csv(self):
        dataframe = pd.read_csv(self.csv_file)
        dataframe.to_sql(self.table_name, self._engine, if_exists='append', index=False)
