#Algorítmo 4: determinar si un número ingresado es primo o no

def determinar_primo(numero):
    divisores = 0
    primo = False
    for i in range(2, numero):
        if numero % i == 0:
            divisores += 1

    if divisores <= 1:
        primo = True
    print(primo)
numero = int(input("Ingrese un número entero: "))
print(determinar_primo(numero))