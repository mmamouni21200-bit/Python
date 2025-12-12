"""Crear una llista dels 10 primers números elevats a una potència donada. 
Utilitzar list comprehensions. 
Ex: Si volem el quadrat dels números de la llista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 
retorni [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], si la volem del cub retorni [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] i així successivament.
"""
def potencies(exponent):
    """
    Retorna una llista dels 10 primers números elevats a la potència donada
    """
    return [num ** exponent for num in range(10)]

# Exemples d'ús:
print("Quadrats:", potencies(2))
print("Cubs:", potencies(3))
print("Potència de 7:", potencies(7))