from estudiantes import estudiantes




for item in estudiantes:
    for key, value in item.items():
        if key == "legajo":
            print("\n")
        print(key , value)



# for item in estudiantes:
#     for indice, nombre in enumerate(item.values()):
#         print(indice, nombre)