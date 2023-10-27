import datetime


class Logger:
    def __init__(self, name: str):
        self.name = name

    def info(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{self.name}] [{timestamp}] INFO: {message}")

    def error(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{self.name}] [{timestamp}] ERROR: {message}")

    def debug(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{self.name}] [{timestamp}] DEBUG: {message}")

    def warning(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{self.name}] [{timestamp}] WARNING: {message}")
