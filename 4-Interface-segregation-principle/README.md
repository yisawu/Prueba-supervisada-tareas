# Interface Segregation Principle (ISP)

Este principio se enfoca en la creación de interfaces específicas para los clientes, en lugar de una única interfaz grande que contenga métodos no utilizados por todos los clientes.

Es decir, es preferible contar con muchas interfaces que definan poco métodos que tener una interfaz forzada a implementar muchos métodos a los que no dará uso.

Esto es para evitar que las clases implementen métodos innecesarios y, en su lugar, define interfaces más pequeñas y cohesivas que se ajusten a las necesidades de cada cliente.

## Ejemplo

Tenemos una interfaz llamada **Impresora** que tiene dos métodos: **imprimir** y **escanear**. Luego tenemos dos clases que implementan esta interfaz, pero cada una solo necesita implementar un método.
