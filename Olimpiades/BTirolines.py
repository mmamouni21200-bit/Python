
n = int(input())
for i in range(n):
    s = input()
    x = s.split()
    h2 = int(x[0]) * int(x[0])
    b2 = int(x[1]) * int(x[1])
    c = h2 + b2
    a=int (c **0.5)
    print(a)
