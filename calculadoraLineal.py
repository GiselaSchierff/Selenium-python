num1 = int(input("Ingrese el primer númmero: "))
num2 = int(input("Ingrese el segundo númmero: "))

operacion = input("Ingrese la operación a realizar: ")

esSuma = operacion == "+"
esResta = operacion == "-"
esDivision = operacion == "/"
esMultiplicacion = operacion == "*"

suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2

if esSuma == True:
    print(f"El resultado es {suma}")
elif esResta == True:
    print(f"El resultado es {resta}")
elif esDivision == True:
    print(f"El resultado es {division}")
elif esMultiplicacion == True:
    print(f"El resultado es {multiplicacion}")
else:
    print(f"Ha ingresado una operación no válida, por favor vuelva a intentarlo")