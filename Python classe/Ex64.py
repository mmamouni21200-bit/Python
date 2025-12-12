"""Crear una funció que donades dues llistes, les concateni amb un connector. Utilitzar zip. 
Ex: [‘sub’,’supra’] i [‘campió’ ‘campiona’] i el connector ‘-’, retorni [‘sub-campió’][‘supra-campiona’].
"""
def concatena_amb_connector(llista1, llista2, connector):
    return [a + connector + b for a, b in zip(llista1, llista2)]
print(concatena_amb_connector(['sub', 'supra'], ['campió', 'campiona'], '-'))