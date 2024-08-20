from abc import ABC, abstractmethod

from app.backend.src.base.application.events.file_event import FileEvent


class FileHandler(ABC):
    @abstractmethod
    def on_file_created(self, event: FileEvent):
        pass

    @abstractmethod
    def on_file_modified(self, event: FileEvent):
        pass
