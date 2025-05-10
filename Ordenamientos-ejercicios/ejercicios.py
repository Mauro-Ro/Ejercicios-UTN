


abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


def ordenamiento_nombres(nombres: list)->list:
    primer_letra = []

    ordenar = []
    name_list = []
    letra = ""

    for i in range(len(nombres)):
        name_list = nombres[i]
        letra += str(name_list[0]).lower()

    for i in letra:
        primer_letra.append(i)
    
    
    for i in range(len(abecedario)):
        for j in range(len(nombres)):
            if primer_letra[j] == abecedario[i]:
                ordenar.append(nombres[j])

    return ordenar

print(ordenamiento_nombres(nombres))