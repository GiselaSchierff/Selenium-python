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


def calculadoraModular(): 
        try:
            num1 = float(input("Ingrese el primer número: "))
        except ValueError as e: 
            print(f"Error: {e}")

        try:
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError as e: 
            print(f"Error: {e}")

        operacion = input("Ingrese la operación a realizar: ")

        esSuma = operacion == "+"
        esResta = operacion == "-"
        esDivision = operacion == "/"
        esMultiplicacion = operacion == "*"
        if esSuma == True:
            resultado = Sumar(num1, num2)
            print(f"El resultado es: {resultado}")
        elif esResta == True:
            resultado = Restar(num1, num2)
            print(f"El resultado es: {resultado}")
        elif esDivision == True:
            resultado = Dividir(num1, num2)
            print(f"El resultado es: {resultado}")
        elif esMultiplicacion == True:
            resultado = Multiplicar(num1, num2)
            print(f"El resultado es: {resultado}")
        else:
            print(f"Ha ingresado una operación no válida, por favor vuelva a intentarlo")


if __name__ == "__main__": 
    calculadoraModular()