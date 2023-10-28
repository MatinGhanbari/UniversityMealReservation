from src.data_access.repositories.user_repository import UserRepository
from src.domain.user import User
from src.infrastructure.config import Config, MongoConfig, RedisConfig
from src.infrastructure.logger import Logger
from src.main import container


class ServiceRegistrar:

    @staticmethod
    def register_services():
        container.register(Config, lambda: Config().load())
        container.register(Logger, lambda: Logger("UniversityMealReservation"))
        container.register(User, lambda: User())
        mongo_configs = container.resolve(Config).mongo
        container.register(MongoConfig, lambda: MongoConfig(mongo_configs['host'], mongo_configs['port'],
                                                            mongo_configs['username'], mongo_configs['password'],
                                                            mongo_configs['database']))
        redis_configs = container.resolve(Config).redis
        container.register(RedisConfig, lambda: RedisConfig(redis_configs['host'], redis_configs['port'],
                                                            redis_configs['password']))

        container.register(UserRepository, lambda: UserRepository(container.resolve(MongoConfig),
                                                                  container.resolve(RedisConfig)))
