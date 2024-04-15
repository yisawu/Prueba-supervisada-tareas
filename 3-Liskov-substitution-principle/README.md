# Liskov Substitution Principle (LSP)

Este principio establece que los objetos deben poder ser reemplazados por instancias de sus subtipos sin alterar el correcto funcionamiento del sistema.

Dicho de forma simple, si tienes una clase base y una clase derivada que hereda de ella, deberías poder usar objetos de la clase derivada en cualquier lugar donde se esperen objetos de la clase base sin alterar el comportamiento del programa.

## Ejemplo

Tenemos una clase base llamada **Figura** y dos clases derivadas llamada **Rectángulo** y **Cuadrado**. El principio de sustitución de Liskov se aplicaría si se puede usar un objeto de la clase **Rectángulo** o de la clase **Cuadrado** en cualquier lugar donde se espera un objeto de la clase **Figura** sin cambiar el comportamiento del programa.
