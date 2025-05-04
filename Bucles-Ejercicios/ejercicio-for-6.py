"""
Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
"""

for i in range(10):
    i = i+1 
    resto = 3*i
    if resto % 3 == 0:
        print(f"El multiplo de 3 es: {resto}")