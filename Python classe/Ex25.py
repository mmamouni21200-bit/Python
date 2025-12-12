"""Definir una funció que utilitzi crear_punts() i dibuixi una imatge per la pantalla."""
def crear_punts(llista):
    for num in llista:
        print('.' * num)
crear_punts([2, 3, 4, 5, 4, 3, 2])