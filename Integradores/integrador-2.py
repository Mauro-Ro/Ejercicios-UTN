
cant_jugadores = True
jugando = False

jugadores = 0
puntos = 0

juga_categorias = 0

linea_separ = "\n---------------------------------------------------------\n"

while cant_jugadores:

    print(linea_separ)
    jugadores = int(input("Ingrese cuantos van a jugar: "))

    if jugadores <= 0:
        print(linea_separ)
        print("Los jugadores no pueden ser menores a 0 (si desea salir ponga 0)")
        print(linea_separ)
        jugadores = int(input("Ingrese cuantos van a jugar: "))
        if jugadores <= 0:
            cant_jugadores = False
        else:
            jugando = True
    else: 
        jugando = True


    for i in range(jugadores):
        print(linea_separ)
        nombre = str(input("Ingrese su nombre: ")).lower()
        edad = int(input("\nIngrese su edad: "))
        
        while edad < 18 or edad > 70: 
            print(linea_separ)
            print("Debes ser mayor de edad")
            print(linea_separ)
            edad = int(input("\nIngrese su edad: "))

        puntos = int(input("\nIngrese sus puntos, no mayor a 60: "))

        while puntos > 60 or puntos < 0:
            print(linea_separ)
            print("Tus puntos no pueden ser menores a 0, o mayores a 60")
            print(linea_separ)
            puntos = int(input("\nIngrese sus puntos, no mayor a 60: "))

        parti_ganadas = int(input("\nIngrese partidas ganadas: "))

        while parti_ganadas < 0 or parti_ganadas > 35:
            print(linea_separ)
            print("Las partidas ganadas no pueden ser menores a 0 o mayores a 35")
            print(linea_separ)
            parti_ganadas = int(input("\nIngrese partidas ganadas: "))

        tipo_saque = input("\nIngrese tipo de saque (Plano, Liftado, Cortado): ").lower()

        while tipo_saque != "plano" and tipo_saque != "liftado" and tipo_saque != "cortado":
            print(linea_separ)
            print("Error ingrese el tipo de saque (Plano, Liftado, Cortado)")
            print(linea_separ)
            tipo_saque = input("\nIngrese tipo de saque: ").lower()

        categoria = input("\nIngrese la categoria (elite, experto, avanzado): ").lower()

        while categoria != "elite" and categoria != "experto" and categoria != "avanzado": 
            print(linea_separ)
            print("Error ingrese la categoria correcta (elite, experto, avanzado)")
            print(linea_separ)
            categoria = input("\nIngrese la categoria: ").lower()

        if categoria == "elite" and tipo_saque == "plano" and (edad >= 19 or edad <= 25):
            juga_categorias += 1 

     
    cant_jugadores = False

print(juga_categorias)

    
