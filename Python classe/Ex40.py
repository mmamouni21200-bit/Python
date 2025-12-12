"""Escriure un programa que calculi en quan s'hauria convertit el nostre capital al final dels anys. Per això li hem de demanar a l’usuari que introdueixi la quantitat a sol·licitar (mínim 50000€ màxim 800000€), un interès (mínim 0.5% i màxim 13%) i el número d’anys (mínim 3 anys - màxim 40 anys).  La fórmula per calcular-ho és: Cfinal = Cinicial * (1 + interés/100) **
  anys.  Ex. 10000€ a 4.5% d’interés a 20 anys s’ha de convertir en 24117.14€"""
def calcular_capital_final(capital_inicial, interès, anys):
    capital_final = capital_inicial * (1 + interès / 100) ** anys
    return capital_final 
# Sol·licitar dades a l'usuari
capital_inicial = float(input("Introdueix la quantitat a sol·licitar (mínim 50000€ màxim 800000€): "))
while capital_inicial < 50000 or capital_inicial > 800000:
    capital_inicial = float(input("Quantitat invàlida. Introdueix una quantitat entre 50000€ i 800000€: ")) 
interès = float(input("Introdueix l'interès (mínim 0.5% i màxim 13%): "))
while interès < 0.5 or interès > 13:
    interès = float(input("Interès invàlid. Introdueix un interès entre 0.5% i 13%: "))
anys = int(input("Introdueix el número d'anys (mínim 3 anys - màxim 40 anys): "))
while anys < 3 or anys > 40:
    anys = int(input("Número d'anys invàlid. Introdueix un número entre 3 i 40: "))
# Calcular i mostrar el capital final
capital_final = calcular_capital_final(capital_inicial, interès, anys)
print(f"El capital final després de {anys} anys serà: {capital_final:.2f}€")
