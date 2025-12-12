"""Crear un directori dins /home/cicles/AO que es digui Prova, canviar-nos a aquest directori,
 a dins, crear el fitxer Ex12.txt i posar a dins el nom de tots els companys de classe. 
 Tancar el fitxer. Obrir-lo per afegir el nom dels professors. Tancar-lo. Finalment, l’obrirem i posarem tot el seu contingut dins una llista de noms.
"""
import os
def gestionar_fitxer(): 
    directori = '/home/cicles/AO/Prova'
    nom_fitxer = 'Ex12.txt'
    ruta_fitxer = os.path.join(directori, nom_fitxer)

    # Crear el directori si no existeix
    os.makedirs(directori, exist_ok=True)

    # Crear i escriure els noms dels companys de classe
    noms_companys = ['Anna', 'Berta', 'Carles', 'David']  # Exemple de noms
    with open(ruta_fitxer, 'w', encoding='utf-8') as fitxer:
        for nom in noms_companys:
            fitxer.write(nom + '\n')

    # Afegir els noms dels professors
    noms_professors = ['Eva', 'Ferran']  # Exemple de noms de professors
    with open(ruta_fitxer, 'a', encoding='utf-8') as fitxer:
        for nom in noms_professors:
            fitxer.write(nom + '\n')

    # Llegir el contingut del fitxer i posar-lo dins una llista
    llista_noms = []
    with open(ruta_fitxer, 'r', encoding='utf-8') as fitxer:
        llista_noms = [linia.strip() for linia in fitxer.readlines()]

    return llista_noms
# Exemple d'ús
noms = gestionar_fitxer()
print("Noms al fitxer:")
for nom in noms:
    print(nom)     
