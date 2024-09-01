import pandas as pd

from app.backend.src.base.domain.contracts.import_csv_contract import ImportCsv


class PandasAdapter(ImportCsv):
    def __init__(self, engine, csv_file: str, table_name: str, dtypes: dict = None):
        self._engine = engine
        self.csv_file = csv_file
        self.table_name = table_name
        self.dtypes = dtypes

    def import_csv(self, if_exists: str = 'append'):
        dataframe = pd.read_csv(self.csv_file)
        dataframe.index.name = 'id'
        if if_exists == 'replace':
            dataframe.to_sql(self.table_name, self._engine, if_exists='replace', index=True, dtype=self.dtypes)
        else:
            dataframe.to_sql(self.table_name, self._engine, if_exists='append', index=False, dtype=self.dtypes)
