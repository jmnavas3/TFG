from abc import ABC, abstractmethod


class ImportCsv(ABC):
    # db entity model name
    _entity_model: str = None

    @abstractmethod
    def import_csv(self):
        """A repository must implement an import_csv method"""
        pass
