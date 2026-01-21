n = int(input())
for i in range(n):
    t=int(input())
    s=input()
    l = s.split()
    l2= []
    for e in l:
        l2.append(int(e))
    l2.sort()
    max = l2[-1:]
    qua = l2.count(max[0])
    print(max[0],qua)
    