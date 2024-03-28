# Open-Close Principle (OCP)

Este principio se refiere a que una entidad de sofware debe quedar abierta para su expansión, pero cerrada para su modificación. Es decir, deberiamos ser capaces de agregar nuevas clases y métodos sin modificar el compartamiento de los ya existentes.

Dependiendo del lenguaje de programación utilizado, esto se logra generalmente utilizando la herencia, la composición, la implementación de interfaces o el uso de patrones de diseño.

## Ejemplo

El ejemplo es sobre un modulo que calcula el área de un circulo. Pero tiempo después, vemos la necesidad de calcular el área de un triángulo.

Una posible solución para esto es, dentro del método calcularArea(), utilizar la condición `if` para averiguar qué tipo de figura es y utilizar la fórmula para calcular el área de la figura correspondiente. Pero esta solución rompe con el principio al ser un método propenso a la modificación constante.

Por lo que, una posible solución que cumpla con el principio es utilizar herencia y polimorfismo. En este caso, el ejemplo se hizo en el lenguaje C++.
