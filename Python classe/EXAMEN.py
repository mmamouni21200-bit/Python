from functools import reduce
def add(x, y):
    return x + y:
ln=[]
sortir='n'
while sortir!='s':
    numero=float(input("\n Introdueix un número: "))
    ln.append(numero)
    sortir=input("\n Vols sortir? (s/n)?")

sumapsitius=reduce(add, [n for n in ln if n>0])
sumanegatius=reduce(add, [n for n in ln if n<0])
print("""Suma de números positius {}
         Suma de números negatius {}
         Mitjana {}""".format(sumapsitius, sumanegatius, (sumapositius+sumanegatius)/len(ln)))

