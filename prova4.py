#a= [1, "a", "Capça",[2], 1, "a"]
a = [10,9,8,7,6,5,1,2,3,4]
print(str(a))





"""
a.remove([2])
a[0]= "Hola, som en Ramis"
a.insert(-2,[3, 2])
a.append(10)
a.append("Cadena nova")
a.append([10,11,12])
a.extend([10, "Cadena nova"])
"""




a= [1, 3, 5, 7, "a", "Capça", [2, 3, 4]]
for e in a:
    print(e)
for i in range(len(a)):
    a[i]*=2 # --> a[i]= a[i]*2
    print("la posició {} té el valor {}", format(i,a(i)))
for i,e in enumerate(a):
    print("la posició {} té el valor {}", format(i,e))
