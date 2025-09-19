def Sumar(a, b):
    suma = a + b
    return suma

def Restar(a, b):
    resta = a - b
    return resta

def Dividir(a, b):
    try: 
        division = a / b
        return division
    except ZeroDivisionError as e: 
        print(f"Error: {e}")

def Multiplicar(a, b):
    multiplicacion = a * b
    return multiplicacion
