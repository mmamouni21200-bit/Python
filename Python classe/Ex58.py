"""Definir una funció elements_parells() que donada una llista de paraules, 
només ens mostri les que estan en la posició parell. Prova-la"""
def elements_parells(llista):
    return [llista[i] for i in range(0, len(llista), 2)]
print(elements_parells(["MOHA", "BARBER", "MEJOR", "ADEU", "JOAN", "HOLA"]))

