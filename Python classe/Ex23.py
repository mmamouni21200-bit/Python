"""Definir una funció crear_repetits() que agafi un número enter i un caràcter i retorni el caràcter multiplicat pel número enter.
 Ex: crear_repetits(5, “a”), retorni “aaaaa”"""

def crear_repetits(numero, caracter):
    return caracter * numero

print(crear_repetits(5, "a"))  # "aaaaa"
print(crear_repetits(3, "*"))  # "***"
print(crear_repetits(2, "-"))  # "--"
print(crear_repetits(0, "x"))  # ""   