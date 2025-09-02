Feature: Prueba de funcionalidad de una calculadora
Scenario: Sumar dos números y validar resultado
Given dado que se ingresaron los números 5 y 4
When se suman ambos numeros
Then el resultado de la suma debe ser siempre 9

Scenario: Restar dos números y validar resultado
Given dado que se ingresaron los números 10 y 6
When se restan ambos numeros
Then el resultado de la resta debe ser siempre 4