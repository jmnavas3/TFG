from abc import ABC, abstractmethod
from app.backend.src.base.application.command.command_interface import CommandInterface


class HandlerInterface(ABC):

    @abstractmethod
    def execute(self, command: CommandInterface):
        pass
