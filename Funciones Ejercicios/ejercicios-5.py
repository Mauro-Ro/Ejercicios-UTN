"""
Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la 
función Restar en sus 4 combinaciones. 
 Restar1(int, int)->int: 
 Restar2()->int: 
 Restar3(int, int): 
 Restar4():
"""

def restar1(num1, num2)->int:
    resta = 0
    resta = num1-num2
    return resta


def resta2()->int:
    resta = 0
    ingrese1 = int(input("ingrese un num: "))
    ingrese2 = int(input("ingrese un num: "))
    resta = ingrese1 - ingrese2
    return resta

# def resta3(num1, num2):

