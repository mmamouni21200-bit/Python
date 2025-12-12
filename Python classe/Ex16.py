"""Definir una funció gran_de_tres(), 
donats tres números, retorni el major. Prova-la amb diferents exemples."""
def fgrandetres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c    
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
num3 = float(input("Introdueix el tercer número: "))
print("El número més gran és: {}".format(fgrandetres(num1, num2, num3)))    