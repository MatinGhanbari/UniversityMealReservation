from src.infrastructure.config import Config


class ServiceRegistrar:
    def __init__(self, container):
        self.container = container

    def register_services(self):
        # Register the Config class
        self.container.register(Config, lambda: Config().load())
