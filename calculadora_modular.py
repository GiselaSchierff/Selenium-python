import operaciones 

def calculadora_modular(): 
        try:
            num1 = float(input("Ingrese el primer número: "))
        except ValueError as e: 
            print(f"Error: {e}")

        try:
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError as e: 
            print(f"Error: {e}")

        operacion = input("Ingrese la operación a realizar: ")

        es_suma = operacion == "+"
        es_resta = operacion == "-"
        es_division = operacion == "/"
        es_multiplicacion = operacion == "*"
        
        if es_suma:
            resultado = operaciones.Sumar(num1, num2)
            return f"El resultado es: {resultado}"
        elif es_resta:
            resultado = operaciones.Restar(num1, num2)
            return f"El resultado es: {resultado}"
        elif es_division:
            resultado = operaciones.Dividir(num1, num2)
            return f"El resultado es: {resultado}"
        elif es_multiplicacion:
            resultado = operaciones.Multiplicar(num1, num2)
            return f"El resultado es: {resultado}"
        else:
            return f"Ha ingresado una operación no válida, por favor vuelva a intentarlo"

# agregar error al dividir por cero? ver guia 4

if __name__ == "__main__": 
    calculadora_modular()