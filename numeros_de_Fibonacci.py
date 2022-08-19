'''
El siguiente es un programa que presenta los n primeros números de Fibonacci
'''
n = int(input("Ingrese un número mayor o igual a 1: "))
fibonacci = [1,1]

def calc_fibonacci(n):
    if n < 1:
        raise ValueError("El número ingresado es menor a 1")
    elif n == 1:
        return fibonacci[0]
    elif n == 2:
        return fibonacci
    else:
        i = 2
        while i < n:
            fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
            i += 1
    return fibonacci

print(calc_fibonacci(n))
