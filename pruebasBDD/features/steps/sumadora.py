from behave import *
from  calculadora import *

@given('dado que se ingresaron los números {num01} y {num02}')
def step_impl(context, num01, num02):
    context.num01 = int(num01)
    context.num02 = int(num02)

@when('se suman ambos numeros')
def step_impl(context):
    miCalculadora = Calculadora(context.num01, context.num02)
    context.sum =  miCalculadora.suma()

@when('se restan ambos numeros')
def step_impl(context):
    miCalculadora = Calculadora(context.num01, context.num02)
    context.sum =  miCalculadora.resta()
    

@then('el resultado de la suma debe ser siempre {res}')
def step_impl(context, res):
    print(res)
    print(context.sum)
    assert context.sum is int(res)

@then('el resultado de la resta debe ser siempre {res}')
def step_impl(context, res):
    print(res)
    print(context.sum)
    assert context.sum is int(res)

