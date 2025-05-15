


def alta_producto(nombre: str, cant: int, matriz: list):
    casillero_cant = 15

    for fila in matriz:
        for columna in fila:
            if columna[0] != None:
                casillero_cant -= 1
            
    if casillero_cant == 0:
        print("No hay mas casilleros ")
        return 
    else:

        for fila in matriz:
            for columna in fila:
                if columna[0] == nombre:
                    print(f"El Producto ya esta agregado en la gondola, casilleros restantes: {casillero_cant}")
                    return
                
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j][0] == None and matriz[i][j][1] == 0:
                    matriz[i][j][0] = nombre
                    matriz[i][j][1] = cant
                    print(f"Producto '{nombre}' agregado en posición [{i}][{j}], casilleros restantes: {casillero_cant}")
                    return






def baja_producto(nombre: str):
    pass

def modificar_producto(nombre: str, fila: int, columna: int):
    pass

