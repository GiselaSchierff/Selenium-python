import operaciones as operacion 

import pytest


def test_suma():
    assert operacion.sumar(1,2) == 3

@pytest.mark.exception
def test_division_por_cero():
    with pytest.raises(ValueError): # ZeroDivisionError
        operacion.dividir(10,0)

@pytest.mark.parametrize("a, b, esperado",
                         [(1, 2, 3),  # positivos enteros 
                          (-1, -2, -3), # negativos enteros 
                          (.25, .25, .50), # positivos decimales 
                          (-.25, -.25, -.50)]) # negativos decimales 
def test_suma_parametrize(a, b, esperado):
    assert operacion.sumar(a, b) == esperado 

def test_resta_con_fixture(numeros_enteros): 
    a, b = numeros_enteros
    assert operacion.restar(a, b) == -1

def test_multiplicacion_con_fixture(numeros_enteros): 
    a, b = numeros_enteros
    assert operacion.multiplicar(a,b) == 12

def test_division_simple():
    assert operacion.dividir(6,2) == 3

def test_multiplicacion_simple(): 
    assert operacion.multiplicar(6,3) == 18

@pytest.mark.smoke
def test_suma_con_fixture(numeros_decimales): 
    a, b = numeros_decimales
    assert operacion.sumar(a, b) == .3 # pytest.approx(.3, rel=1e-4)
