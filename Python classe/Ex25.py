"""Definir una funció que utilitzi crear_punts() i dibuixi una imatge per la pantalla.
Definir una funció gran_llista() que donada una llista de número ens retorni el més gran. Ex: gran_llista([3, 4, 2, 3, 10]), retorni 10."""
def fcrear_punts(llista):
    for num in llista:
        print('.' * num)
def gran_llista(llista):
    max_num = llista[0]
    for num in llista:
        if num > max_num:
            max_num = num
    return max_num
# Exemple d'ús de les funcions
fcrear_punts([1, 3, 5, 2])
print("El número més gran de la llista és:", gran_llista([3, 4, 2, 3, 10]))