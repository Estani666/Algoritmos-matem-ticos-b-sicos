#Algorítmo 3: Encontrar todos los divisores de un número dado

def find_proper_divisors(value):
    divisors = [1]
    for i in range(2, value):
        if value % i == 0:
            divisors.append(i)
    print(divisors)

value = int(input("Digite un número: "))
print(find_proper_divisors(value))