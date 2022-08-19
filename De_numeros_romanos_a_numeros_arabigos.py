valor_arabigo = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000}
numero_romano = input("Ingrese un número romano: ")

def de_numero_romano(numero_romano):
    valor = 0
    valor_ultimo_digito = 0
    for digito_romano in reversed(numero_romano):
        valor_digito = valor_arabigo[digito_romano]
        modo_suma = valor_digito >= valor_ultimo_digito
        if modo_suma:
            valor += valor_digito
            valor_ultimo_digito = valor_digito
        else:
            valor -= valor_digito
    return valor

print(de_numero_romano(numero_romano))