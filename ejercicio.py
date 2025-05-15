
tablero = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1]
    ]

contador = 0


def verificar_cordenadas(tablero: list, x: int,y: int)->bool:
    if tablero[x][y] == 0:
        print("disparó en el agua")
        return False
    else:
        print("barco hundido")
        return True

def pedir_cordenadas(x:int, y:int):
    global contador
    if x > 4 or y > 4:
        print("Cordendas fuera de rango")
    else:
        if verificar_cordenadas(tablero, x, y) == True:
            contador += 1


def preguntar_batalla():
    entrada = input("ingrese (si/no) para jugar: ")
    while entrada.lower() == "si":
        x = int(input("ingrese x: "))
        y = int(input("ingrese y: "))
        pedir_cordenadas(x, y )
        entrada = input("ingrese (si/no) para jugar: ")
        print(f"\n barcos hundidos: {contador}\n")
    


preguntar_batalla()