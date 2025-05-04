"""
Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
el número ingresado. Mostrar la cantidad de divisores encontrados.
"""

entrada = int(input("Ingrese un numero: "))

cant_div = 0
divisores = ""
num = 1

while num <= entrada:
    if entrada % num == 0:
        divisores += str(num)+", "
        cant_div += 1 
    num+=1


print(f"Divisores: {divisores}")
print(f"Cantidad de divisores: {cant_div}")