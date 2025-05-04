"""
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero. 

Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
"""

input_1 = int(input("Ingrese el primer numero: "))
input_2 = int(input("Ingrese el segundo numero: "))
input_3 = int(input("Ingrese el tercer numero: "))
input_4 = int(input("Ingrese el cuarto numero: "))
input_5 = int(input("Ingrese el quinto numero: "))

suma = 0

pares = 0
impares = 0

menor = 0

if (input_1 %2) == 0 :
    pares+=1
else: 
    impares+=1

if (input_2 %2) == 0 :
    pares+=1
else: 
    impares+=1

if (input_3 %2) == 0 :
    pares+=1
else: 
    impares+=1
        
if (input_4 %2) == 0 :
    pares+=1
else: 
    impares+=1

if (input_5 %2) == 0 :
    pares+=1
else: 
    impares+=1


if input_1 < input_2 and input_1 < input_3 and input_1 < input_4 and input_1 < input_5:
    menor = input_1
elif input_2 < input_3 and input_2 < input_3 and input_2 < input_4 and input_2 < input_5:    
    menor = input_2
elif input_3 < input_2 and input_3 < input_1 and input_3 < input_4 and input_3 < input_5:
    menor = input_3
elif input_4 < input_1 and input_4 < input_2 and input_4 < input_3 and input_4 < input_5:
    menor = input_4
else:
    menor = input_5


    

print(f"pares: {pares}")
print(f"impares: {impares}")
print(f"El menor es: {menor}")