"""

Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
Debe retornar las veces que la letra está incluida en el texto.

"""
texto = "Desarrollar una función que reciba una letra y una cadena."
def cantidad_letras_cadenas(letra: str, cadena: str)-> int:
    """
    Cuenta cuántas veces aparece una letra específica dentro de una cadena de texto.

    Args:
        letra (str): Letra a buscar (debe ser un solo carácter).
        cadena (str): Texto en el que se va a buscar la letra.

    Returns:
        int: Cantidad de veces que la letra aparece en la cadena.
    """      
    cantidad = 0
    for i in range(len(cadena)):
        if cadena[i] == letra:
            cantidad += 1

    return cantidad

print(cantidad_letras_cadenas("r", texto))


"""

Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
Si las posiciones no son válidas se debe informar.

"""

texto = "Desarrollar una función que reciba una letra y una cadena."

def subcadena_por_indice(indice_1: int,indice_2: int, cadena: str)->str:
    """
    Devuelve una subcadena desde indice_1 hasta indice_2 (sin incluir indice_2),
    si los índices son válidos.

    Args:
        indice_1 (int): Índice inicial.
        indice_2 (int): Índice final (no incluido).
        cadena (str): Cadena de texto original.

    Returns:
        str: Subcadena resultante o mensaje de error si los índices no son válidos.
    """    
    validacion = cadena[indice_1 : indice_2]

    if indice_1 < 0 or indice_2 > len(cadena) or indice_1 >= indice_2:
        validacion = "debe contener una cadena"
    return validacion
print(subcadena_por_indice(0, 11,texto))


"""
Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
**IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
<número de caracteres> - 1.
"""


def char_at(cadena: str, numero: int)-> str:
    """
    Devuelve el carácter en la posición indicada por el número, si es válida.

    Args:
        cadena (str): Cadena de caracteres de la cual se quiere obtener un carácter.
        numero (int): Índice del carácter a obtener.

    Returns:
        str: El carácter en la posición indicada o un mensaje de error si el índice no es válido.
    """    
    if 0 <= numero < len(cadena):
        cadena = cadena[numero]
    else:
        cadena = "Índice fuera de rango"

    return cadena

print(char_at("hola",3))




