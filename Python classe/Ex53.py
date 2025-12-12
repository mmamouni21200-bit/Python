"""Definir una funció index_paraula() on donada una llista ordenada de paraules,
 ens retorni l’índex on es troba una paraula determinada o -1 en cas que no hi sigui."""
def index_paraula(llista, paraula):
    """
    Retorna l'índex d'una paraula en una llista ordenada de paraules.
    
    Args:
        llista: Llista ordenada de paraules
        paraula: Paraula a cercar
        
    Returns:
        int: Índex de la paraula si es troba, -1 en cas contrari
    """
    for index, element in enumerate(llista):
        if element == paraula:
            return index
    return -1
# Prova de la funció
llista_paraules = ["apple", "banana", "cherry", "date", "fig", "grape"]
paraula_cercada = "cherry"
index = index_paraula(llista_paraules, paraula_cercada)
if index != -1:
    print(f"La paraula '{paraula_cercada}' es troba a l'índex: {index}")
else:
    print(f"La paraula '{paraula_cercada}' no es troba a la llista.")
# Prova amb una paraula que no està a la llista
paraula_cercada = "orange"
index = index_paraula(llista_paraules, paraula_cercada)
if index != -1:
    print(f"La paraula '{paraula_cercada}' es troba a l'índex: {index}")
else:
    print(f"La paraula '{paraula_cercada}' no es troba a la llista.")