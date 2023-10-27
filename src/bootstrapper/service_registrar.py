from src.infrastructure.config import Config
from src.infrastructure.logger import Logger


class ServiceRegistrar:
    def __init__(self, container):
        self.container = container

    def register_services(self):
        # Register the Config class
        self.container.register(Config, lambda: Config().load())
        self.container.register(Logger, lambda: Logger("UniversityMealReservation"))
