from src.services.Service import ServiceInterface
from winter.decorators import Service, Primary


@Service
class FirstServiceImpl(ServiceInterface):

    def __init__(self):
        if not issubclass(type(self), ServiceInterface):
            raise NotImplementedError("Not a valid implementation")

    def process(self, name):
        return f"{name} is processing", 3.14


@Primary
@Service
class ServiceImpl(ServiceInterface):

    def __init__(self):
        if not issubclass(type(self), ServiceInterface):
            raise NotImplementedError("Not a valid implementation")

    def process(self, name):
        return f"{name} is processing", 3.141593
