"""Definir una funció hi_ha_duplicats() que ens indiqui si una llista donada té 
qualque element duplicat o no, no s’ha de modificar la llista donada. Prova-la.
"""
def hi_ha_duplicats(llista):
    """
    Comprova si una llista té elements duplicats.
    
    Args:
        llista: Llista de elements a comprovar
        
    Returns:
        bool: True si hi ha duplicats, False en cas contrari
    """
    elements_vistos = set()
    for element in llista:
        if element in elements_vistos:
            return True
        elements_vistos.add(element)
    return False
# Proves amb diferents llistes
print("=" * 50)
print("PROVES DE LA FUNCIÓ hi_ha_duplicats()")
print("=" * 50)
# Casos amb duplicats
print("\n--- AMB DUPLICATS ---")
print(f"hi_ha_duplicats([1, 2, 3, 2]): {hi_ha_duplicats([1, 2, 3, 2])}")
print(f"hi_ha_duplicats(['a', 'b', 'c', 'a']): {hi_ha_duplicats(['a', 'b', 'c', 'a'])}")
print(f"hi_ha_duplicats([True, False, True]): {hi_ha_duplicats([True, False, True])}")
# Casos sense duplicats
print("\n--- SENSE DUPLICATS ---")
print(f"hi_ha_duplicats([1, 2, 3, 4]): {hi_ha_duplicats([1, 2, 3, 4])}")
print(f"hi_ha_duplicats(['x', 'y', 'z']): {hi_ha_duplicats(['x', 'y', 'z'])}")
print(f"hi_ha_duplicats([False, True]): {hi_ha_duplicats([False, True])}") 
# Casos amb llista buida i un sol element
print("\n--- CASOS ESPECIALS ---")
print(f"hi_ha_duplicats([]): {hi_ha_duplicats([])}")
print(f"hi_ha_duplicats([42]): {hi_ha_duplicats([42])}")  
print(f"hi_ha_duplicats(['únic']): {hi_ha_duplicats(['únic'])}")