"""Definir una funció gran_llista() que donada una llista de número ens retorni 
el més gran. Ex: gran_llista([3, 4, 2, 3, 10]), retorni 10."""
def gran_llista(llista_numeros):
    numero_mes_gran = llista_numeros[0]
    for numero in llista_numeros:
        if numero > numero_mes_gran:
            numero_mes_gran = numero
    return numero_mes_gran 
# Exemple d'ús de la funció
llista = [3, 4, 2, 3, 10]
print("El número més gran és:", gran_llista(llista))