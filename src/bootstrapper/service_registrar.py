from src.infrastructure.config import Config
from src.infrastructure.container import Container

container = Container()

# Register the Config class
container.register(Config, lambda: Config().load())
