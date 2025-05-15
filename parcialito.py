"""
    Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos):

Realizar el juego de la Batalla Naval
Dado el siguiente tablero con los barcos ubicados de la siguiente forma:
tablero = [ 
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1]]

Pedirle una coordenada al usuario para la fila (x) [validar 0-4]
Pedirle una coordenada al usuario para la columna (y) [validar 0-4]

Desarrollar una función con el siguiente prototipo:
    verificar_coordenadas(tablero: list, x: int, y: int) -> bool:
La función debe retornar "True" si el barco fue hundido (1) y "False" si disparó en el agua (0)
Según lo retornado por la función, mostrar al usuario los siguientes mensajes:
    "Hundido"   "Agua"

El usuario puede realizar tantos disparos como quiera, cuando no quiera seguir disparando, se le debe informar cuántos barcos fueron hundidos.

Nota: No se pueden utilizar funciones propias.
"""



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
    

if __name__ == "__main__":
    preguntar_batalla()