import json

import telegram._update

from src.data_access.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, mongo_config, redis_config):
        super().__init__(mongo_config, redis_config)
        self.users_collection = self.mongo_db['users']

    def find_one(self, id: str):
        if self.redis_client.get(str(id)) is not None:
            return json.loads(self.redis_client.get(str(id)))
        return self.users_collection.find_one({'_id': id})

    def insert_one(self, update: telegram._update.Update):
        document = {
            "_id": update.message.from_user.id,
            "first_name": update.message.from_user.first_name,
            "last_name": update.message.from_user.last_name,
            "username": update.message.from_user.username
        }
        self.users_collection.insert_one(document)

    def delete_one(self, id):
        self.users_collection.delete_one({'_id': id})
