#include <iostream>
#include <cmath>

// Ejemplo con el principio de abierto/cerrado aplicado.

// Clase base abstracta para las formas geométricas
class FormaGeometrica {
public:
    virtual double calcularArea() const = 0;
    virtual ~FormaGeometrica() {} // Destructor virtual para la clase base
};

// Implementación concreta para un triángulo
class Triangulo : public FormaGeometrica {

private:
    double _base;
    double _altura;

public:
    Triangulo(double base, double altura) : _base(base), _altura(altura) {}

    double calcularArea() const override {
        return 0.5 * _base * _altura;
    }
};

// Implementación concreta para un círculo
class Circulo : public FormaGeometrica {

private:
    double _radio;
    
public:
    Circulo(double radio) : _radio(radio) {}

    double calcularArea() const override {
        return M_PI * _radio * _radio;
    }
};

// Clase principal que calcula el área de una forma geométrica sin conocer su implementación concreta
class CalculadoraArea {

private:
    const FormaGeometrica& _forma;

public:
    CalculadoraArea(const FormaGeometrica& forma) : _forma(forma) {}

    double calcular() const {
        return _forma.calcularArea();
    }

};

// Ejecución del código
int main() {
    Triangulo triangulo(5.0, 3.0);
    Circulo circulo(2.0);

    CalculadoraArea calculadoraTriangulo(triangulo);
    std::cout << "Área del triángulo: " << calculadoraTriangulo.calcular() << std::endl;

    CalculadoraArea calculadoraCirculo(circulo);
    std::cout << "Área del círculo: " << calculadoraCirculo.calcular() << std::endl;

    return 0;
}
