from src.data_access.repositories.user_repository import UserRepository
from src.infrastructure.config import Config, MongoConfig, RedisConfig
from src.infrastructure.logger import Logger


class ServiceRegistrar:
    def __init__(self, container):
        self.container = container

    def register_services(self):
        # Register the Config class
        self.container.register(Config, lambda: Config().load())
        self.container.register(Logger, lambda: Logger("UniversityMealReservation"))
        self.container.register(UserRepository, lambda: UserRepository())
        mongo_configs = self.container.resolve(Config)['mongo']
        self.container.register(MongoConfig, lambda: MongoConfig(mongo_configs['host'], mongo_configs['port'],
                                                                 mongo_configs['username'], mongo_configs['password'],
                                                                 mongo_configs['database']))
        redis_configs = self.container.resolve(Config)['redis']
        self.container.register(RedisConfig, lambda: RedisConfig(redis_configs['host'], redis_configs['port'],
                                                                 redis_configs['password']))
