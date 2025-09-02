Feature: Probaremos ingreso de usuario
Scenario: Se probará ingreso de datos correctos
Given Dado el nombre lbravo y password 123456
When presiona boton ingresar
Then debe decir 1

Scenario: Se probará ingreso de datos ingreso incorrectos
Given Dado el nombre lbravo y password 123455
When presiona boton ingresar
Then debe decir 0

Scenario: Se probará ingreso de login incorrecto
Given Dado el nombre lbravoy y password 123456
When presiona boton ingresar
Then debe decir 0