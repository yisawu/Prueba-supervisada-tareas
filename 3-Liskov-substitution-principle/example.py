# Clase base
class Figura:
    def area(self):
        pass

#clase derivada
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

#clase derivada
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

def calcular_area(figura):
    print("El área de la figura es:", figura.area())

# Usando el principio de sustitución de Liskov
rectangulo = Rectangulo(5, 4)
cuadrado = Cuadrado(5)

calcular_area(rectangulo)
calcular_area(cuadrado)
