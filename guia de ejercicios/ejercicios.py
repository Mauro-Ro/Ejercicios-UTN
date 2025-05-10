"""
Ejercicio 1: Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su  
sueldo para esa persona.
"""


# nombre = input("Ingrese nombre: ")

# sueldo = int(input("Ingrese sueldo: "))

# incremento = sueldo+(sueldo*0.1)

# print(f"Se le aumento un 10% el sueldo a: {nombre} y en total quedaria: {incremento}")



"""
Pedir una edad.  Informar si la persona es mayor de edad (más de 18 años), 
adolescente (entre 13 y 17 años) o niño (menor a 13 años). 
"""

# edad = int(input("Ingrese edad: "))

# if edad > 17:
#     print("es mayor de edad")
# elif edad < 17 and edad > 12:
#     print("es adolescente")
# else:
#     print("es niño")


"""
Ingresar 5 números enteros, distintos de cero.
Informar: 
a. Cantidad de pares e impares. 
b. El menor número ingresado. 
c. De los pares el mayor número ingresado. 
d. Suma de los positivos. 

e. Producto de los negativos.
"""

# pares = 0
# impares = 0
# menor = 0
# par_num = 0
# par_mayor = 0
# sum_positivos = 0
# produc_negati = 1



# entra_nums = 5
# for i in range(5):
#     ingrese = int(input(f"Ingrese 5 números enteros, distintos de cero: "))

#     if ingrese % 2 == 0:
#         pares += 1
#         if pares == 1:
#             par_mayor = ingrese
#         else:
#             par_num = ingrese
#     else:
#         impares += 1

#     if par_num > par_mayor:
#         par_mayor = par_num

#     if menor == 0:
#         menor = ingrese
    
#     if ingrese > 0:
#         sum_positivos += ingrese

#     if ingrese < 0:
#         produc_negati *= ingrese

#     if menor > ingrese:
#         menor = ingrese


# print(f"Pares: {pares}, Impares: {impares}")
# print(f"Menor: {menor}")
# print(f"Mayor par: {par_mayor}")
# print(f"Suma positivos: {sum_positivos}")
# print(f"Producto negativos: {produc_negati}")

"""
Ejercicio 4: Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil 
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO 
ser soltero.' 
"""

# edad = int(input("Ingrese su edad: "))

# estado_civil = input("Ingrese su estado civil: ").lower()


# if edad < 18 and estado_civil != "soltero":
#     print("Es muy pequeño para NO ser soltero.")


"""
Ejercicio 5: Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 
por cada estadía como base, se pide el ingreso de una estación del 
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del 
Plata/Córdoba) para vacacionar para poder calcular el precio final: 

-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un 
descuento del 10% Mar del Plata tiene un descuento del 20% 

-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene 
un aumento del 10% Mar del Plata tiene un aumento del 20% 

-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un 
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el 
precio sin descuento. Validar el ingreso de datos
"""


# tarifa_base = 15000

# estacion_anio = input("Ingrese una estación del año (Invierno/Verano/Otoño/Primavera): ").lower()
# localidad = input("Ingrese una localidad (Bariloche/Cataratas/Mar del Plata/Córdoba): ").lower()

# if estacion_anio == "invierno" : 
#     if localidad == "bariloche":
#         tarifa_base = tarifa_base + (tarifa_base * 0.20)
#         print(tarifa_base)
#     elif localidad == "cataratas" or localidad == "cordoba":
#         tarifa_base = tarifa_base - (tarifa_base * 0.10)
#         print(tarifa_base)
#     elif localidad == "mar del plata":
#         tarifa_base = tarifa_base - (tarifa_base * 0.20)
#         print(tarifa_base)
#     else:
#         print("Localidad inválida.")

# elif estacion_anio == "verano":
#     if localidad == "bariloche":
#         tarifa_base = tarifa_base - (tarifa_base * 0.20)
#         print(tarifa_base)
#     elif localidad == "cataratas" or localidad == "cordoba":
#         tarifa_base = tarifa_base + (tarifa_base * 0.10)
#         print(tarifa_base)
#     elif localidad == "mar del plata":
#         tarifa_base = tarifa_base + (tarifa_base * 0.20)
#         print(tarifa_base)
#     else:
#         print("Localidad inválida.")

# elif estacion_anio == "otoño" or estacion_anio == "primavera":
#     if localidad == "bariloche":
#         tarifa_base = tarifa_base + (tarifa_base * 0.10)
#         print(tarifa_base)
#     elif localidad == "cataratas":
#         tarifa_base = tarifa_base + (tarifa_base * 0.10)
#         print(tarifa_base)
#     elif localidad == "mar del plata":
#         tarifa_base = tarifa_base + (tarifa_base * 0.10)
#         print(tarifa_base)
#     elif localidad == "cordoba":
#         print(tarifa_base)
#     else:
#         print("Localidad inválida.")

# else:
#     print("Estación inválida.")
