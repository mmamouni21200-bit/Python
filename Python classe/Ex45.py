"""Escriure un programa que sumi els dígits d’un número donat i ens digui si la seva suma és parell o senar.
"""
num = input("Introdueix un número: ")
suma = 0
for digit in num:
    suma += int(digit)
if suma % 2 == 0:
    print("La suma dels dígits és {} i és parell.".format(suma))
else:
    print("La suma dels dígits és {} i és senar.".format(suma)) 
    