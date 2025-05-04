"""
Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La 
función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el 
programa principal realizando la invocación o llamada. 
"""

def determinas_num(num: int)->bool:
    par = True
    if num %2 == 0:
        par = True
    else:
        par = False
    return par


print(f"es par: {determinas_num(7)}")