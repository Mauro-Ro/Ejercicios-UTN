"""
Realizar una función recursiva que calcule la suma de los primeros números naturales:
"""

def sumar_naturales(numero: int)->int:
    if numero == 0:
        return numero
    else: 
        return numero + sumar_naturales(numero -1)


print(sumar_naturales(5))