"""Escriure un programa on li passem un número (mínim 1 i màxim 900000) i ens indiqui la quantitat de dígits que té."""
def comptar_digits(numero):
    if numero < 1 or numero > 900000:
        return "El número ha d'estar entre 1 i 900000."
    contador = 0
    while numero > 0:
        numero //= 10
        contador += 1
    return contador
# Exemple d'ús de la funció
numero = 12345
print("El número té", comptar_digits(numero), "dígits.")
