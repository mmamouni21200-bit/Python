"""Escriure un programa que mostri els dígits parells d’un número donat.
"""
num = input("Introdueix un número: ")
print("Els dígits parells són: ", end='')
for digit in num:
    if int(digit) % 2 == 0:
        print(digit, end=' ')