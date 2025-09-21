import operaciones as operacion # VER SI ESTO FUNCIONA 

import pytest


def test_suma():
    assert operacion.sumar(1,2) == 3

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        operacion.dividir(10,0)

@pytest.mark.parametrize("a, b, esperado",
                         [(1, 2, 3),  # positivos enteros 
                          (-1, -2, -3), # negativos enteros 
                          (.25, .25, .50), # positivos decimales 
                          (-.25, -.25, -.50)]) # negativos decimales 
def test_suma_parametrize(a, b, esperado):
    assert operacion.sumar(a, b) == esperado 

def test_resta_con_fixture(numeros): 
    a, b = numeros
    assert operacion.restar(a, b) == -1

def test_suma_con_fixture(numeros): 
    a, b = numeros
    assert operacion.sumar(a,b) == 7