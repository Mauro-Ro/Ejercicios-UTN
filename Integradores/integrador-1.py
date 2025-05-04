num_encues = 0
encuesta_1 = 0
encuesta_2 = 20
cant_encuestas = 10
votos_encues = ""


while num_encues < cant_encuestas:
    print(f"\n--------------- Encuesta numero {num_encues} ---------------\n")

    nombre = str(input("Ingrese su nombre: ")).lower()
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:

        genero = str(input("Ingrese su género (Masculino - Femenino - Otro): ")).lower()
        tecnologia = str(input("Ingrese su tecnologia (IA, RV/RA, IOT): ")).lower()
        
        tecno_valida = tecnologia == "iot" or tecnologia == "ia"

        if genero == "masculino" and tecno_valida and edad >= 25 and edad <= 50:
            encuesta_1 += 1
    
        if tecnologia != "ia" and (genero == "femenino" or (edad >= 33 and edad <= 40)):
            encuesta_2 += 1

        if genero == "masculino" and edad >= 18:
            votos_encues = f"Votos de la encuesta 3: {nombre}, {tecnologia}"
        
        num_encues +=1
    else:
        print("Tienes que ser mayor")        

porcentaje_encues = (encuesta_2 / cant_encuestas)*100


print(f"Cantidad de empleados de género masculino que votaron por IOT o IA: {encuesta_1}")
print(f"Porcentaje de empleados que no votaron por IA: {porcentaje_encues}%")
print(votos_encues)