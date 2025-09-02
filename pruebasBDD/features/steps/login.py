#ejecutar en directorio features con behave login.features

from behave import *
@given('Dado el nombre {nombre} y password {password}')
def step_impl(context, nombre, password):
    context.nombre = str(nombre)
    context.password = str(password)

@when('presiona boton ingresar')
def step_impl(context):
    context.resultado = 0
    print('Nombre : ',context.nombre)
    print('Password : ',context.password)
    if context.nombre == 'lbravo' and context.password == '123456':
       context.resultado = 1


@then('debe decir {res}')
def step_impl(context, res):
    print('<<<<<Resultado: >>>>>',context.resultado)
    print('<<<<<res>>>> ', res)
    print(context.resultado == res)
    assert context.resultado is int(res)
