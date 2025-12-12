"""Definir una funció que donada una cadena, avaluï quantes lletres majúscules hi ha. Prova-la amb diferents exemples."""
def comptar_majuscules(cadena):
    contador = 0
    for caràcter in cadena:
        if caràcter.isupper():
            contador += 1
    return contador
# Exemple d'ús de la funció
cadena1 = "HolaMón"
cadena2 = "python és Genial"
print(f"La cadena '{cadena1}' té {comptar_majuscules(cadena1)} lletres majúscules.")
print(f"La cadena '{cadena2}' té {comptar_majuscules(cadena2)} lletres majúscules.")
cadena3 = "AQUESTA ÉS UNA FRASE EN MAJÚSCULES"
print(f"La cadena '{cadena3}' té {comptar_majuscules(cadena3)} lletres majúscules.")
cadena4 = "aquesta és una frase en minúscules"
print(f"La cadena '{cadena4}' té {comptar_majuscules(cadena4)} lletres majúscules.")