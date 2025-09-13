"""
# CLASE 1

print('¡Hola Automation Tester!')

# CLASE 2

# actividad 1 

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
profesion = input("Escribe tu profesión: ")

print(f"Hola {nombre}, de profesión {profesion} y de {edad} años")



# actividad 2

contador = 0
for i in range (100): 
    if i % 2 == 0: 
        print(i)
        contador +=1
        if contador == 10: 
            break 

numero = 0
contador = 0
while contador < 10: 
    if numero % 2 == 0: 
        print(numero)
        contador +=1 
    numero += 1

igual = 5 is 5 # evalua el valor y el tipo de dato 
print(igual)



for i in range(0,11,1): 
    if i == 5:
        break
    print(i)
   
for i in range(0,11,1): 
    if i == 5:
        continue
    print(i)""" 
 
i = 1
while i <=5:
    print(i)
    i = i + 1