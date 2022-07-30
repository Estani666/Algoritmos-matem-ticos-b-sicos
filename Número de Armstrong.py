'''
El siguiente programa tiene por objetivo determinar si un número ingresado es un número de Armstrong.
'''
numero = int(input("Ingrese un número entero: "))
prueba = numero
digitos = 0
suma = 0
i = 0
numero_separado = [int(a) for a in str(numero)] #Se separa el número en cifras

#Determinar la cantidad de digitos que posee el número ingresado
while prueba > 1:
    prueba = prueba/10
    digitos += 1
while i <= (digitos-1):
    operacion = numero_separado[i] ** digitos
    suma = operacion + suma
    i += 1
if suma == numero:
    print("Es un número de Armstrong.")
else:
    print("NO es un número de Armstrong.")




