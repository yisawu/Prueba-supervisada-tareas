from abc import ABC, abstractmethod

class Impresora(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass
    
    @abstractmethod
    def escanear(self, documento):
        pass

class ImpresoraSimple(Impresora):
    def imprimir(self, documento):
        print(f"Imprimiendo {documento}")

class EscanerSimple(Impresora):
    def escanear(self, documento):
        print(f"Escanenado {documento}")

# Ejemplo de uso
if __name__ == "__main__":
    impresora = ImpresoraSimple()
    escaner = EscanerSimple()

    impresora.imprimir("Documento1")
    escaner.escanear("Documento2")
