from .utils import import_string


class Config(dict):
    def __init__(self, defaults=None):
        super().__init__(defaults or {})

    def from_object(self, obj):
        if isinstance(obj, str):
            obj = import_string(obj)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)
