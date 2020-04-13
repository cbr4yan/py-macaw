from .config import Config


class Macaw:
    def __init__(self, name):
        self.name = name
        self.is_running = False
        self.config = Config()

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False
