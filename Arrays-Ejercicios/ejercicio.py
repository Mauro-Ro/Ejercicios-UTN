from listas_personas import nombres as lista_nombres
from listas_personas import country, telefonos, postalZip, mails, edades, address, region


"""

Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.

"""



# def llamar_nombres(nombres_lista: list)->list:
#     """
#     Parametros:
#         nombres_lista (list): Es una lista donde va a guardar nombres.

#     Retorna:
#         list: Retorna la lista con los 10 nombres ingresados.

#     """
#     while len(nombres_lista) < 11:
#         nombres = input("Igrese 10 Nombres: ")
#         nombres_lista += [nombres]
#     return nombres_lista

# print (llamar_nombres())



"""

Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida
posición y número a guardar al usuario, lo guarde en una lista en la posición
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
función y mostrar por pantalla el retorno.

"""


# def listar_numeros(posicion: int, guardar_num: int,)->list:
#     """
#     Parametros:
#         posicion (int): la posicion en la lista donde se sumara el numero.
#         guardar_num (int): el numero que se va a agregar en la lista.

#     Retorna:
#         list: la lista resultante con el numero agregado.
#     """

#     num_list = [0] * 10 

#     for i in range(len(num_list)):
#         if posicion == i:
#             num_list[posicion] += guardar_num
#             return num_list

    
# print(listar_numeros(2, 4))



"""

Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango
especificado, validar los números solicitados dentro de ese rango, guardar en una
lista y retornarla. El programa principal debe invocar a la función y mostrar por
pantalla el retorno.

"""



# def pedir_rango_nums()->list:
#     """
#     Parametros:
#         sin parametros formales.

#     Retorna:
#         list: la lista resultante con los numeros agregados.
#    """

#     rango_lista = []

#     for i in range(10):
#         ingrese = int(input("Ingrese 10 numeros que esten en el rango de 10 a 100: "))

#         while ingrese < 10 or ingrese > 100:
#             print("Numero fuera del rango")
#             ingrese = int(input("Ingrese 10 numeros que esten en el rango de 10 a 100: "))

#         if ingrese > 10 or ingrese < 100:   
#             rango_lista += [ingrese]
 

#     return rango_lista



# print(pedir_rango_nums())



"""

Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números
y un número especificado. La misma debe buscar el número especificado en la lista
y retornar “True” si existe.

"""


# def buscar_numeros(lista: list, num: int)->bool:
#     """
#         Parametros:
#             list: lista de numeros en la que se buscara el valor.
#             num: numero que se desea verificar si existe en la lista.

#         Retorna:
#             bool: True si num esta en lista, False en caso contrario.
#     """
    
#     valor = False

#     for i in range(len(lista)):
#         if lista[i] == num:
#             valor = True

#     return valor

    

# print(buscar_numeros([2, 3, 4], 4))



"""

Ejercicio 5: Dadas las siguientes listas:
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, busque a las
personas de menor edad (puede ser más de una) y las retorne. El programa
principal deberá mostrar nombre y edad de los menores.

"""

# nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


# def verificador_edad(nombre: list, edad: list)->str:
#     """
#         Parametros:
#             nombre: se debe proporcionar una lista con nombres para que puedan ser mostrados.
#             edad: es importante que haya una lista con edades para identificar los menores.

#         Retorna:
#             str: retorna los menores de edad en foramto string.
#     """
#     menor = ""
#     for i in range(len(edad)):
#         if edad[i] < 18:
#             menor += nombre[i]+" "+ str(edad[i])+", "

#     return menor


# print(verificador_edad(nombres, edades))



"""

Ejercicio 6: Analizar los datos del archivo listas_personas.py Utilizando el archivo
listas_personas.py Importar los nombres a una lista. Realizar una función que
muestre los mismos.

"""


# def mostrar_nombres(nombre: list):
#     """
#         Parametros:
#             nombre: se debe proporcionar una lista con nombres para que puedan ser mostrados.

#         Retorna:
#             no retorna nada.
#     """
#     lista_nombres = []
#     for i in range(len(nombre)):
#         lista_nombres += [nombre[i]]
#     print(lista_nombres)

# mostrar_nombres(lista_nombres)


"""

Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de
compras on-line recientemente lanzado al mercado para ello necesita un programa
que le permita acceder a los datos relevados.

"""

""" 2-Listar los datos de los usuarios de México """

def usuarios_mexicanos(nombres: list)->list:
    users_mexico = []

    for i in range(len(nombres)):
        if country[i] == "Mexico":
            users_mexico += [nombres[i], country[i]]

    return users_mexico

# print(usuarios_mexicanos(lista_nombres, country))

""" 3-Listar los nombre, mail y teléfono de los usuarios de Brasil """

def usuarios_brasil(country: list)->list:
    users_brasil = []

    for i in range(len(country)):
        if country[i] == "Brazil":
            users_brasil += [lista_nombres[i], country[i], telefonos[i], mails[i]]


    return users_brasil

# print(usuarios_brasil(country))

""" 4-Listar los datos del/los usuario/s más joven/es """

def usuarios_jovenes(edad: list)->list:
    users_jovenes = []

    for i in range(len(edad)):
        if edad[0] >= edad[i]:
            users_jovenes += [lista_nombres[i], edad[i]]

    return users_jovenes

# print(usuarios_jovenes(edades))

""" 5-Obtener un promedio de edad de los usuarios """

def promedio_edades(edad: list)->int:
    promedio = 0

    for i in range(len(edad)):
        promedio += int(edad[i])


    promedio = promedio/len(edad)

    return int(promedio)


# print(promedio_edades(edades))

""" 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad """

def edad_mayor_br(edades: list)-> int:
    edad_mayor = 1
    mayor_lista = []

    for i in range(len(edades)):
        if country[i] == "Brazil" and edades[i] >= edad_mayor:
            edad_mayor = edades[i]
            mayor_lista += [lista_nombres[i], edad_mayor]
    return mayor_lista

# print(edad_mayor_br(edades))


""" Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000  """


def datos_mx_br(country: list)->list:
    datos_list_mexico = []


    for i in range(len(country)):
        if country[i] == "Mexico" or country[i] == "Brazil" and (postalZip[i] >= 8000):
            datos_list_mexico += [lista_nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]]

    return datos_list_mexico

# print(datos_mx_br(country))


""" 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años. """


def listar_italianos(lista: list)->list:
    datos_italianos = []

    for i in range(len(lista)):
        if country[i] == "Italy" and edades[i] >= 40:
            datos_italianos += [lista_nombres[i], mails[i], telefonos[i]]

    return datos_italianos


# print(listar_italianos(country))


def lineas_hori(tipo: str, cant: int):
    lineas = ""

    for i in range(cant*3):
        lineas += tipo 

    print(lineas)