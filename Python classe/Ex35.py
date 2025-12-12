"""Definir una funció comptar_vocals() que donada una paraula, compti el número de vegades que apareix cada vocal. 
Ex: comptar_vocals(“Ratapinyada”) retorni1 HI ha 4 a’s, 0 e’s, 1 i’s, 0 o’s i 0 u’s."""
def comptar_vocals(paraula):
    vocals = 'aeiouAEIOU'
    comptador = {vocal: 0 for vocal in vocals}
    
    for char in paraula:
        if char in comptador:
            comptador[char] += 1
    
    for vocal in 'aeiou':
        total = comptador[vocal] + comptador[vocal.upper()]
        print(f"Hi ha {total} {vocal}'s") 
# Exemple d'ús de la funció
paraula = "Moha barber"
comptar_vocals(paraula)