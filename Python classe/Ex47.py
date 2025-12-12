"""Definir una funció eliminarcapicua() que donada una llista, elimini el primer
 i el darrer element de la llista i ens retorni una nova llista sense aquest dos elements. Prova-la
"""
def eliminarcapicua(llista):
    if len(llista) <= 2:
        return []
    else:
        return llista[1:-1]
llista = [int(x) for x in input("Introdueix una llista d'elements separats per espais: ").split()]
nova_llista = eliminarcapicua(llista)
print("Llista original:", llista)
print("Llista després d'eliminar el primer i l'últim element:", nova_llista)