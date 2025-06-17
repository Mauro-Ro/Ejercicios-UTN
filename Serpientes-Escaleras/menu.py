from Preguntas.preguntas import *
from Preguntas.funciones import *



tablero = [
    0, 1, 0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 2, 1, 1, 2, 1, 0, 1, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0]


def menu():
    run = True
    inicio = 15
    input_nombre = input("ingrese su nombre: ")
    lista_nums = []
    while run:
        
        validar = validacion_entrada("Desea seguir jugando responda (si/no): ", "error")

        if validar == "no":
            run = False
        
        numero_elegido = numero_random(lista_preguntas)

        buscar_pregunta(numero_elegido)

        validar_respuesta(numero_elegido)

        


        lista_nums.append(numero_elegido)

        if len(lista_nums) == 15:
            run = False


if __name__ == '__main__':
    menu()