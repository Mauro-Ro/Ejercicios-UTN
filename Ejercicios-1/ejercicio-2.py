"""
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
"""

input_edad = int(input("Ingrese la edad: "))

if (input_edad >= 18):
    print("Es mayor de edad")
elif (input_edad <= 17 and input_edad >= 13):
    print("Eres adolescente")
else:
    print("Eres niño")