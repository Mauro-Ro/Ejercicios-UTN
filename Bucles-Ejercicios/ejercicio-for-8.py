"""
Realizar un programa que permita mostrar una pirámide de números. Por
ejemplo: si se ingresa el numero 5, la salida del programa será la
siguiente:
"""

entrada = int(input("Ingrese un numero: "))

concatenar = ""

for i in range(entrada):
    i+=1
    concatenar += str(i)
    print(concatenar)