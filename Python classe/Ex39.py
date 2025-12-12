"""Escriure un programa que demani dues paraules i ens digui si rimen o no. Rimen quan coincideixen les 3 darreres lletres i 
rimen un poc quan coincideixen les 2 darreres, si no ens ha de dir que no rimen."""
def rimen(paraula1, paraula2):
    if paraula1[-3:] == paraula2[-3:]:
        return "Rimen"
    elif paraula1[-2:] == paraula2[-2:]:
        return "Rimen un poc"
    else:
        return "No rimen"
# Exemple d'ús de la funció
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")
print(rimen(paraula1, paraula2))
