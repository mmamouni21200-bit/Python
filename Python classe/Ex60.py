"""Escriu un programa que ens indiqui tots els números primers entre 1 i 100 i ens digui quants n’hi ha."""
def es_primer(num):
    
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


primers = []


print("Números primers entre 1 i 100:")


for numero in range(1, 101):
    if es_primer(numero):
        primers.append(numero)
        print(numero, end=" ")

print(f"\nTotal de números primers entre 1 i 100: {len(primers)}")