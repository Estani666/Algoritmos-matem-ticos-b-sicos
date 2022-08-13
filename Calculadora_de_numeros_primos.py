'''
El siguiente es un programa que muestra todos los números primos hasta un número ingresado por
el usuario
'''
numero = int(input("Ingrese un número: "))
numeros_primos = []

def calc_numeros_primos(numero):
    i = 2
    while i <= numero:
        a = 2
        contador_divisores = 0
        while a < i:
            if i % a == 0:
                contador_divisores += 1
            a += 1
        if contador_divisores == 0:
            numeros_primos.append(i)
        i += 1
    return numeros_primos

print(calc_numeros_primos(numero))
