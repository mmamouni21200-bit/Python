"""Crear una funció que compti la longitud de cada paraula d’una cadena de caràcters que li passem.
 Utilitzar map. Ex: def lenp(frase): -- retorni una llista amb la longitud de cada paraula de la frase.
"""
def lenp(frase):
    return list(map(len, frase.split()))
print(lenp("Hola sóc Moha barber"))
