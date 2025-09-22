def sumar(a, b):
    suma = a + b
    return suma

def restar(a, b):
    resta = a - b
    return resta

def dividir(a, b):
        division = a / b # la posición de esta linea cambia el tipo de error
        # Si se pone antes salta el error de dividir por cero y se atrapa con el ZeroDivisionError
        # Si se pone después, ese error no pasa porque lo ataja el ValueError 
        if b == 0:
            raise ZeroDivisionError("Error al dividir por cero")  
        return division

        

def multiplicar(a, b):
    multiplicacion = a * b
    return multiplicacion
