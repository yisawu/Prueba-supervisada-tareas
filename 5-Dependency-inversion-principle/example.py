from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Logger(LoggerInterface):
    def log(self, message):
        print(message)

class Usuario:
    def __init__(self, nombre, logger: LoggerInterface):
        self.nombre = nombre
        self.logger = logger

    def saludar(self):
        self.logger.log(f'Hola, soy {self.nombre}')

logger = Logger()
usuario = Usuario('Juan', logger)
usuario.saludar()
