'''
Por definición, un número natural se llama número perfecto si su valor es igual a la suma de sus divisores. Esto es verdad, por ejemplo,
para el número 6 y 28:

1 + 2 + 3 = 6
1 + 2 + 4 + 7 + 14 = 28

La siguiente es una calculadora de números perfectos en la que se ingresa un número dado y se evaluan los números anteriores a tal número
para imprimir todos los números perfectos que aparecen en el recorrido
'''

numero = int(input("Ingrese un número: "))
numeros_perfectos = []

def calc_numero_perfecto(numero):
    i = 0
    while i < numero:
        a = 1
        divisores = []
        while a <= i:
            if i % a == 0:
                divisores.append(a)
            a += 1
            if a == i and sum(divisores) == i:
                numeros_perfectos.append(i)
        i += 1
    return numeros_perfectos

print(calc_numero_perfecto(numero))
