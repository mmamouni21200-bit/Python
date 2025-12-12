"""Definir una funció gran() que, donats dos números, retorni el major.  Prova-la amb diferents exemples.""" 
def fgrandedos(a,b):
    if a >= b:
        return a
    else:
        return b 
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
print("El número més gran és: {}".format(fgrandedos(num1, num2)))
