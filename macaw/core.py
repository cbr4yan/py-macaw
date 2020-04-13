from .config import Config
from .defaults import defaults


class Macaw:
    def __init__(self, name):
        self.name = name
        self.is_running = False
        self.config = Config(defaults)

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False
