


abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



def ordenamiento_nombres(nombres: list, edades: list)->list:
    ordenar = []
    edades_ordenadas = []


    primer_letra = []
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
                edades_ordenadas.append(edades[j])

    return ordenar, edades_ordenadas








