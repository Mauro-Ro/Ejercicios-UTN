""" 
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
"""
input_nombre = str(input("Ingrese su nombre: "))

input_sueldo = float(input("Ingrese su sueldo: "))

sueldo_aumen = (input_sueldo * 0.10) + input_sueldo

print(f"El sueldo de {input_nombre} a sido incrementado un 10% en total quedaria en: {sueldo_aumen}")

