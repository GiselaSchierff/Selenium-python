def sumar(a, b):
    suma = a + b
    return suma

def restar(a, b):
    resta = a - b
    return resta

def dividir(a, b):
        division = a / b
        if b == 0:
             raise ZeroDivisionError("Error al dividir por cero") 
        return division

        

def multiplicar(a, b):
    multiplicacion = a * b
    return multiplicacion
