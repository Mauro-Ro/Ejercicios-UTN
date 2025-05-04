




def calcular_fibonacci(num: int)->int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return calcular_fibonacci(num -1 ) + calcular_fibonacci(num -2 )

print(calcular_fibonacci(5))