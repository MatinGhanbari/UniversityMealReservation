import json


class Config:
    def __init__(self):
        self.api_key = None
        self.mongo = None
        self.redis = None

    def load(self):
        # Load the telegram_bot configuration from the file
        with open("../config.json", "r") as f:
            config = json.load(f)

        # Set the telegram_bot's token and prefix
        self.api_key = config["api_key"]
        self.mongo = config["mongo"]
        self.redis = config["redis"]

        # Return the configuration
        return self


class MongoConfig:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database


class RedisConfig:
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
