"""
Crear un programa en Python que:
Construya una matriz de 4 filas x 4 columnas con números fijos (predefinida).
Utilice una función que recorra las columnas de la matriz y verifique,
si existe un número repetido 3 veces de manera vertical (una debajo de otra).
Si lo encuentra, la función debe retornar ese número.
Si no existe, debe retornar None.
# MATRIZ FIJA
matriz = [
    [5, 2, 3, 4],
    [5, 2, 7, 8],
    [2, 2, 3, 1],
    [1, 6, 7, 4]
]
"""

matriz = [
    [5, 2, 3, 4],
    [5, 2, 7, 8],
    [2, 2, 3, 1],
    [1, 6, 7, 4]
]


def repeticion_tres(matriz: list)->any:
    resultado = None

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == matriz[1][j] == matriz[2][j]:
                resultado = matriz[i][j]

    return resultado
 
    


  

print(repeticion_tres(matriz))