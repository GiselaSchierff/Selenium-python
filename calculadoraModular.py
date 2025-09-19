import operaciones 

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
            resultado = operaciones.Sumar(num1, num2)
            print(f"El resultado es: {resultado}")
        elif esResta == True:
            resultado = operaciones.Restar(num1, num2)
            print(f"El resultado es: {resultado}")
        elif esDivision == True:
            resultado = operaciones.Dividir(num1, num2)
            print(f"El resultado es: {resultado}")
        elif esMultiplicacion == True:
            resultado = operaciones.Multiplicar(num1, num2)
            print(f"El resultado es: {resultado}")
        else:
            print(f"Ha ingresado una operación no válida, por favor vuelva a intentarlo")


if __name__ == "__main__": 
    calculadoraModular()