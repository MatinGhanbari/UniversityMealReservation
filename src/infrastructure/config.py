import json


class Config:
    def __init__(self):
        self.api_key = None

    def load(self):
        # Load the telegram_bot configuration from the file
        with open("../config.json", "r") as f:
            config = json.load(f)

        # Set the telegram_bot's token and prefix
        self.api_key = config["api_key"]

        # Return the configuration
        return self
