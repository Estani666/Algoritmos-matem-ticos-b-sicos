#El siguiente es un programa que calcula el factorial de un número
numero = int(input("Ingrese un número: "))

def calc_factorial(numero):
    factorial = 1
    i = 1
    while i <= numero:
        factorial = factorial * 1
        i += 1
    return factorial

print(calc_factorial(numero))