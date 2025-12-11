"Definir una funció paraula_mes_llarga() que donada una llista de paraules, "
"retorni la que té més caràcters. Ex: paraula_mes_llarga([“Hola”, “Ramis”, “IES”, “Paraula”]), ens retorni Paraula."
def paraula_mes_llarga(llista_paraules):
    paraula_llarga = ""
    for paraula in llista_paraules:
        if len(paraula) > len(paraula_llarga):
            paraula_llarga = paraula
    return paraula_llarga
# Exemple d'ús de la funció
llista = ["Hola", "Ramis", "IES", "Paraula"]
print("La paraula més llarga és:", paraula_mes_llarga(llista)) 