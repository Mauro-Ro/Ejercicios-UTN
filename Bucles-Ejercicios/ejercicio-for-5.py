
suma = 0
promedio = 0
for i in range(10):
    entrada = int(input("Ingrese un numero: "))

    suma += entrada

    if entrada == 0:
        promedio = suma / i
        break

print(f"promedio: {promedio}")
print(f"suma: {suma}")