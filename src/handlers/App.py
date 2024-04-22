from src.services.Service import ServiceInterface
from winter.decorators import Component


@Component
class App:

    def __init__(self, service: ServiceInterface, other_service: ServiceInterface, name: str):
        self._service = service
        self._name = name

    def process(self):
        return self._service.process(self._name)


@Component
def app(service: ServiceInterface, service_2: str, name: str):

    return service.process(name)
