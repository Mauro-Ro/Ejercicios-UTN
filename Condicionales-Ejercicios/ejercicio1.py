
menor = 0
par = 0
impar = 0

mayor = 0

for i in range(5):
    ingrese = int(input("Ingrese 5 numeros: "))

    if (ingrese % 2) == 0:
        par += 1
    else:
        impar += 1

    if i == 0:
        menor = ingrese
    elif menor > ingrese:
        menor = ingrese 


    if i == 0:
        mayor = ingrese
    elif mayor < ingrese and (ingrese % 2) == 0:
        mayor = ingrese


print(par)
print(impar)
print(menor)

print(mayor)