for i in range(10,-1,-1):
    print("{} * 5={}".format(i,i*5))
"""

a = int(input("Escriu el primer operand"))
b = int(input("Escriu el segon operand"))
if opcio==1:
    print("La suma de {} + {} és".format(a, b, a+b))
if opcio==2:
    print("La resta de {} - {} és".format(a, b, a-b))
if opcio==3:
    print("La multiplicació de {} * {} és".format(a, b, a*b))
if opcio==4:
    print("La Divisió de {} / {} és".format(a, b, a/b))
if opcio==0:
    print("Sortir")
