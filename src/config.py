# Questão 1

class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'environment'):
            self.environment = 'production'
        if not hasattr(self, 'currency'):
            self.currency = 'BRL'
        if not hasattr(self, 'debug'):
            self.debug = False

    
    