a= float(input("Escriu el primer nombre:"))
b= float(input("Escriu el segon nombre:"))
c= float(input("Escriu el tercer nombre:"))

d=a+b+c
print("El resultat de la suma {} + {} + {} es {}".format(a, b, c, d))
if d> 20:
    print("La suma és major que 20, que és {}".format(d))
else:
    print("La suma és menor que 20, que és {}".format(d))
d=a*b*c
print("El resultat de la multiplicació {} * {} * {} es {}".format(a, b, c, d))
if d> 20:
    print("La multiplicació és major que 20, que és {}".format(d))
else:
    print("La multiplicació és menor que 20, que és {}".format(d))