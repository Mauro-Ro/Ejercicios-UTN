"""
Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5
"""

entrada = int(input("Ingrese un numero: "))


i= 1

multipli = 0
while i <= 10:
    multipli = print(f"{entrada} x {i} = ", entrada*i)
    i+=1