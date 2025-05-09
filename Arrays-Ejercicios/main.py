from listas_personas import country, telefonos, postalZip, mails, edades, address, region, nombres
from ejercicio import usuarios_mexicanos, usuarios_brasil, usuarios_jovenes, promedio_edades, edad_mayor_br, datos_mx_br, listar_italianos, lineas_hori



def menu_opciones():

    entrar =  True
    while entrar:
        lineas_hori("-",20)
        print(
            "\n2 - Lista de los datos de los usuarios de México\n"
            "3 - Lista de los nombres, mails y teléfonos de los usuarios de Brasil\n"
            "4 - Lista de los datos del/los usuario/s más joven/es\n"
            "5 - promedio de edad de los usuarios\n"
            "6 - De los usuarios de brasil, el mayor\n"
            "7 - Usuarios de México y Brasil con código postal mayor a 8000\n"
            "8 - Usuarios italianos mayores a 40 años\n"
            "0 - Salir\n"
        )
        lineas_hori("-", 20)
        opcion = int(input("\nElegí una opción: "))
        volver = True
        while volver:
            lineas_hori("-", 20)
            match opcion:
                case 2:
                    print(f"\n{usuarios_mexicanos(nombres)}\n")
                    ingrese = int(input("0 para volver atras: "))
                    if ingrese == 0:
                        lineas_hori("-", 20)
                        volver = False
                case 3:
                    print(f"\n{usuarios_brasil(country)}\n")
                    ingrese = int(input("0 para volver atras: "))
                    if ingrese == 0:
                        volver = False       
                case 4:
                    print(f"\n{usuarios_jovenes(edades)}\n")
                    ingrese = int(input("0 para volver atras: "))
                    if ingrese == 0:
                        volver = False                   
                case 5:
                    print(promedio_edades(edades))
                    ingrese = int(input("0 para volver atras: "))
                    if ingrese == 0:
                        volver = False                           
                case 6:
                    print(edad_mayor_br(edades))
                    ingrese = int(input("0 para volver atras: "))
                    if ingrese == 0:
                        volver = False       
                case 7:
                    print(datos_mx_br(country))
                    ingrese = int(input("0 para volver atras: "))
                    if ingrese == 0:
                        volver = False       
                case 8:
                    print(listar_italianos(edades))
                    ingrese = int(input("0 para volver atras: "))
                    if ingrese == 0:
                        volver = False       
                case 0:
                    entrar = False
                    volver = False 
                case _:
                    print("\nOpción inválida")
                    volver = False 
            


menu_opciones()

