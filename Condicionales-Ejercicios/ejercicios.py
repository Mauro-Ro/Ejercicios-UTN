

numMenor = 0

entrada1 = int(input("Entrada 1: "))
entrada2 = int(input("Entrada 2: "))
entrada3 = int(input("Entrada 3: "))
entrada4 = int(input("Entrada 4: "))


if entrada1 < entrada2:
    numMenor = entrada1
else: 
    numMenor = entrada2

if entrada3 < numMenor:
    numMenor = entrada3 

if entrada4 < numMenor:
    numMenor = entrada4 

print(numMenor)