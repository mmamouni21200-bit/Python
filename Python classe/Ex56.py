"""Escriure un programa que sumi tots els números entre dos números donats, ambdós inclosos."""
def sumar_entre_dos_numeros(num_inici, num_fi):
    """Suma tots els números entre dos números donats, ambdós inclosos."""
    suma = sum(range(num_inici, num_fi + 1))
    return suma 
# Programa principal
print("=" * 50)
print("    PROGRAMA DE SUMA ENTRE DOS NÚMEROS")
print("=" * 50)
# Sol·licitar els números a l'usuari
num_inici = int(input("Introdueix el primer número (inici): "))
num_fi = int(input("Introdueix el segon número (fi): "))
# Calcular la suma
resultat = sumar_entre_dos_numeros(num_inici, num_fi)
# Mostrar el resultat
print(f"\nLa suma dels números entre {num_inici} i {num_fi} és: {resultat}")
print("\n" + "=" * 50)