"""

1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

"""

def sumar_naturales(numero: int)->int:
    if numero == 0:
        return numero
    else: 
        return numero + sumar_naturales(numero -1)


print(sumar_naturales(5))

"""

2. Realizar una función recursiva que calcule la potencia de un número:

"""


def calcular_potencia(base: int, exponente: int)->int:
    if exponente == 1:
        return base
    else:
        return base * calcular_potencia(base, exponente -1)
    

print(calcular_potencia(2, 3))

"""
3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

"""

def sumar_digitos(numero: int)->int:
    if numero == 0:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)    



print(sumar_digitos(123))


"""

4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La
función deberá seguir el siguiente prototipo:

"""


def calcular_fibonacci(num: int)->int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return calcular_fibonacci(num -1 ) + calcular_fibonacci(num -2 )

print(calcular_fibonacci(5))