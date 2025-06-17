"""
1.Mostrar los números ascendentes desde el 1 al 10
"""


# for i in range(1,11):
#     mostrar = print(i)
    

"""
2.Mostrar los números descendentes desde el 10 al 1
"""

# i = 10 
# while i > 0:
#     print(i)
#     i-= 1

"""
3.Ingresar un número. Mostrar los números desde 0 hasta el número
ingresado.
"""

# entrada = int(input("ingrese un numero: "))

# for i in range(entrada + 1):
#     print(i)


"""
4.Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5
"""

# entrada = int(input("Ingrese un numero: "))

# for i in range(11):
#     print(f"{entrada} x {i} = ", entrada*i)


"""
5.Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
número 0. Mostrar la suma y el promedio de todos los números.
"""

# suma = 0
# promedio = 0
# for i in range(10):
#     entrada = int(input("Ingrese un numero: "))

#     suma += entrada

#     if entrada == 0:
#         promedio = suma / i
#         break

# print(f"promedio: {promedio}")
# print(f"suma: {suma}")


"""
6.Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
"""

# run = True
# i = 0
# resto = 0
# while run:
#     i = i+1 
#     resto = 3*i
#     if resto >= 10:
#         run = False
#     else:
#         if resto % 3 == 0:
#             print(f"El multiplo de 3 es: {resto}")


"""
7.Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
"""

# for i in range(51):
#     if i % 2 == 0:
#         print(f"este es el numero par: {i}")


"""
8.Realizar un programa que permita mostrar una pirámide de números. Por
ejemplo: si se ingresa el numero 5, la salida del programa será la
siguiente:
"""

# entrada = int(input("Ingrese un numero: "))

# concatenar = ""

# for i in range(entrada):
#     i+=1
#     concatenar += str(i)
#     print(concatenar)


"""
9.Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
el número ingresado. Mostrar la cantidad de divisores encontrados.
"""

# entrada = int(input("Ingrese un numero: "))

# cant_div = 0
# divisores = ""
# num = 1

# while num <= entrada:
#     if entrada % num == 0:
#         divisores += str(num)+", "
#         cant_div += 1 
#     num+=1


# print(f"Divisores: {divisores}")
# print(f"Cantidad de divisores: {cant_div}")


"""
10.Ingresar un número. Determinar si el número es primo o no.
"""

# entrada = int(input("Ingrese un numero: "))

# primo = True

# for i in range(entrada):
#     if i > 1:
#         if (entrada % i) == 0 :
#             primo = False
#             break
#         else:
#             primo = True
#     else:
#         continue


# if primo == True:
#     print(f"{entrada} es primo")
# else:
#     print(f"{entrada} no es primo")


"""
11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
número ingresado. Informar cuántos números primos se encontraron.
"""

# entrada = int(input("Ingrese un número: "))

# contador_primos = 0 

# print("Números primos encontrados:")

# for num in range(2, entrada + 1):
#     es_primo = True

#     for i in range(2, num):
#         if num % i == 0:
#             es_primo = False
#             break

#     if es_primo:
#         print(num)
#         contador_primos += 1

# print(f"Cantidad de números primos: {contador_primos}")