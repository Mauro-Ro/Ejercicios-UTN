"""
.Ingresar un número. Determinar si el número es primo o no.
"""

entrada = int(input("Ingrese un numero: "))

primo = True

for i in range(entrada):
    if i > 1:
        if (entrada % i) == 0 :
            primo = False
            break
        else:
            primo = True
    else:
        continue


if primo == True:
    print(f"{entrada} es primo")
else:
    print(f"{entrada} no es primo")