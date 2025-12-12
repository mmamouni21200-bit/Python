"""Definir una funció filtrar_paraules() que donada una llista de paraules i un 
número x, retorni totes les paraules que tingui més d’x-caràcters."""
def filtrar_paraules(llista_paraules, x):
    paraules_filtrades = []
    for paraula in llista_paraules:
        if len(paraula) > x:
            paraules_filtrades.append(paraula)
    return paraules_filtrades
# Exemple d'ús de la funció
llista = ["Hola", "Ramis", "IES", "Paraula", "Python", "Programació"]
x = 4
print("Paraules amb més de", x, "caràcters:", filtrar_paraules(llista, x))  
