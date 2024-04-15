# Dependency Inversion Principle (DIP)

Este principio sugiere que los módulos de alto nivel no deben depender de los módulos de bajo nivel, sino que ambos deben depender de abstracciones. Además, las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstracciones.

Esto se logra a través de interfaces o clases abstractas. Al seguir el DIP, se promueve la flexibilidad y la facilidad de sustitución de componentes, lo que hace que el sistema sea más resistente a los cambios y más fácil de probar.

El objetivo es reducir las dependencias entre los módulos del código, es decir, alcanzar un bajo acoplamiento de las clases.

## Ejemplo

En un sistema donde tenemos una clase **Usuario** que depende de una clase **Logger** para realizar el registro de eventos. Donde la clase **Usuario** depende de la interfaz **LoggerInterface** en lugar de depender directamente de la clase **Logger**, cumpliendo así con el DIP.
