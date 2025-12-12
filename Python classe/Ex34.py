"""Variar l’exercici anterior, perquè enlloc de la lletra a, sigui una lletra introduïda per teclat per l’usuari."""
def nums_que_comencen_per(llista_noms, lletra):
    contador = 0
    for nom in llista_noms:
        if nom.lower().startswith(lletra.lower()):
            contador += 1
    return contador
# Exemple d'ús de la funció
llista = ["Anna", "Bernat", "Alba", "Carles", "Aina"]
lletra = input("Introdueix una lletra: ")
print(f"Nombre de noms que comencen per '{lletra}':", nums_que_comencen_per(llista, lletra))