from abc import ABC, abstractmethod


class LogInput(ABC):

    @abstractmethod
    def retrieveData(self):
        pass


