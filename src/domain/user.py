from src.data_access.repositories.user_repository import UserRepository
from src.main import container


class User:
    def __init__(self):
        self.user_repository = container.resolve(UserRepository)

    def save(self, update):
        self.user_repository.insert_one(update)
