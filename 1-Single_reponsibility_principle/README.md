# Single Responsibility Principle (SRP)

Este es la primera letra de lo que se conoce como principios SOLID. Consiste en que una clase debe tener una única responsabilidad o rol que cumplir y que esta responsabilidad debe estar estar complementamente encapsulada por la clase. De esta manera se hace claro el rol de cada clase y, por ende, facilita la comprensión, el mantenimiento y reutilización del código.

## Ejemplo

Suponga que hay hacer un programa que verifique que los clientes sean de 18 años o mayor y que tengan un nombre.

Si no aplicamos SRP, entonces solo necesitamos crear la clase Client y dentro de dicha clase definir las variables y constructor necesarios y, finalmente, las funciones para hacer la verificación.

Si aplicamos SRP, entonces después de crear la clase Client y definir tanto las variables necesarios como el constructor, hay que crear una nueva clase que contenga las funciones para verificar. La razón es porque la clase Client solo puede tener una única responsabilidad, la de guardar los datos del cliente y por eso hay que crear otra clase que asuma la responsabilidad de verificar los datos.
