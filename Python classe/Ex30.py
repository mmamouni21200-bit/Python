"""Escriure un programa que converteixi el números binaris en enters.
"""
def binari_a_enter(binari):
    enter = 0
    longitud = len(binari)
    for i in range(longitud):
        bit = int(binari[longitud - 1 - i])
        enter += bit * (2 ** i)
    return enter
# Exemple d'ús de la funció
binari = "1101"
print("El número binari", binari, "és l'enter", binari_a_enter(binari))