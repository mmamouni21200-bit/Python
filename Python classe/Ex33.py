"""Definir una funció nums_que_comencen_per() que donat una llista de noms, ens digui quants comencen per la lletra a."""
def nums_que_comencen_per(llista_noms, lletra):
    contador = 0
    for nom in llista_noms:
        if nom.lower().startswith(lletra.lower()):
            contador += 1
    return contador
# Exemple d'ús de la funció
llista = ["Anna", "Bernat", "Alba", "Carles", "Aina"]
lletra = 'a'
print(f"Nombre de noms que comencen per '{lletra}':", nums_que_comencen_per(llista, lletra))