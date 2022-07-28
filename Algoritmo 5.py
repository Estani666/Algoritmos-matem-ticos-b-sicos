#Algorítmo 5: Muestra los números primos en un determinado rango.

def is_prime(potentially_prime):
    for i in range(2, potentially_prime // 2 + 1):
        if potentially_prime % i == 0:
            return False
    return True
primes = []
valor = int(input("Digite un número entero: "))
for number in range(2, valor):
    if is_prime(number):
        primes.append(number)
print("Los números primos hasta el valor digitado son: ")
print(primes)
