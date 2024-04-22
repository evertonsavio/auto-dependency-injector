from abc import ABC


class ServiceInterface(ABC):

    def process(self, name):
        raise NotImplementedError("process() must be implemented")
