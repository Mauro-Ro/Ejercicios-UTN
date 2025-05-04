"""
Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor 
solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a 
dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado 
por pantalla.  Atención: pueden reutilizarse funciones ya creadas. 
"""
def realizarDescuento(num: int):
    descuento =  num-(num*0.05)
    print(descuento)

numero1 = int(input("Ingrese un nuemero: "))

if numero1 < 10 or numero1 > 100:
    print("El numero ingresado debe ser mayor a 10 y/o menor a 100")
else:
    realizarDescuento(numero1)



    