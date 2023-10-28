import pymongo
import redis


class BaseRepository:
    def __init__(self, mongo_config, redis_config):
        self.mongo_config = mongo_config
        self.redis_config = redis_config
        self.redis_client = redis.Redis(
            host=self.redis_config.host,
            port=self.redis_config.port,
            password=self.redis_config.password
        )
        self.mongo_client = pymongo.MongoClient(
            host=self.mongo_config.host,
            port=int(self.mongo_config.port),
            username=self.mongo_config.username,
            password=self.mongo_config.password,
        )
        self.mongo_db = self.mongo_client[self.mongo_config.database]
