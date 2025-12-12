"""Escriure un programa que imprimeixi la taula de multiplicar d’un número donat (mínim 1 màxim 20).
"""
num = int(input("Introdueix un número entre 1 i 20 per veure la seva taula de multiplicar: "))
if 1 <= num <= 20:
    print("Taula de multiplicar del {}:".format(num))
    for i in range(1, 11):
        print("{} x {} = {}".format(num, i, num * i))
else:
    print("Número fora de rang. Si us plau, introdueix un número entre 1 i 20.")
