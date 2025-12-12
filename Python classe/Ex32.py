"""Definir una funció  mostrar_majors_que() que donada una tupla de números enters, imprimeixi tots els superiors a un altre número donat. Per provar que funciona bé, 
escriure un programa que permeti introduir els valors enters de la tupla  i ens digui tots els que són majors de 18 anys."""
def mostrar_majors_que(tupla_numeros, x):
    for numero in tupla_numeros:
        if numero > x:
            print(numero)
# Exemple d'ús de la funció
tupla = (12, 25, 30, 15, 18, 22, 10)
x = 18
print("Números majors que", x, ":")
mostrar_majors_que(tupla, x)   