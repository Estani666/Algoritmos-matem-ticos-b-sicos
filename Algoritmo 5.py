#Algorítmo 5: Muestra los números primos en un determinado rango.

potentially_prime = int(input("Ingrese un número: "))
def is_prime(potentially_prime):
    for i in range(2, potentially_prime): #range(inicio, fin) va desde inicio a fin-1
        if potentially_prime % i == 0:
            return False
        return True
primos = [2, ]
for i in range(2, potentially_prime):
    if is_prime(i):
        primos.append(i)
print(primos)