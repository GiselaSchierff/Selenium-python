num1 = int(input("Ingrese el primer númmero: "))
num2 = int(input("Ingrese el segundo númmero: "))

operacion = input("Ingrese la operación a realizar: ")

es_suma = operacion == "+"
es_resta = operacion == "-"
es_division = operacion == "/"
es_multiplicacion = operacion == "*"

suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2

if es_suma == True:
    print(f"El resultado es {suma}")
elif es_resta == True:
    print(f"El resultado es {resta}")
elif es_division == True:
    print(f"El resultado es {division}")
elif es_multiplicacion == True:
    print(f"El resultado es {multiplicacion}")
else:
    print(f"Ha ingresado una operación no válida, por favor vuelva a intentarlo")