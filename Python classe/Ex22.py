"""Definir una funció superposicio() que agafi dues llistes i retorni vertader si hi ha un element en comú, en cas contrari, que retorni fals.
"""
llista1=[1, 2, 3, 4, 5]
llista2=[6, 7, 8, 9, 10]
def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False
print("Les llistes tenen elements en comú?: {}".format(superposicio(llista1, llista2)))