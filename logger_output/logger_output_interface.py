from abc import ABC, abstractmethod


class LogOutput(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def sendData(self, data):
        pass