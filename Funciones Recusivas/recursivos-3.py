


def sumar_digitos(numero: int)->int:
    if numero == 0:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)    



print(sumar_digitos(123))