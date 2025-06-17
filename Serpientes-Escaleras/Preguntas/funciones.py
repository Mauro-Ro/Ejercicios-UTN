import random
from .preguntas import preguntas


lista_preguntas = list(range(15))


def numero_random(lista: list)->int:

    elegido = random.choice(lista)

    lista.remove(elegido)

    return elegido

def buscar_pregunta(num: int):
    for i, valor in enumerate(preguntas[num].values()):
        if i == 0:
            print(valor)
        elif i == 1:
            print("a.", valor)
        elif i == 2:
            print("b.",valor)
        elif i == 3:
            print("c.",valor)

def buscar_respuesta(num: int)->str:
    respuesta = ""
    for i, valor in enumerate(preguntas[num].values()):
        if i == 4:
            respuesta = valor
    
    return respuesta

def validar_respuesta(num: int):
    respuesta = True
    run = True
    while run:
        ingrese = input("Ingrese su respuesta: ")

        if ingrese.isdigit() == True:
            print("No puede ser un numero")

        
        if buscar_respuesta(num) == ingrese.lower():
            respuesta = True
            run = False
        else:
            respuesta = False
            run = False

    return respuesta

def validacion_entrada(entrada: str, error: str):
    volver = True
    respuesta = ""
    while volver :
        ingrese = input(entrada).lower()
        if ingrese.isdigit() == True:
            print(error)
        else:
            volver = False
        respuesta = ingrese

    return respuesta

