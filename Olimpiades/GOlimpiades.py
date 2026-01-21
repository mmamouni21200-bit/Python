n=int(input())
for _ in range(n):
    m,n=map(int,input().split())
    temps=[]
    for i in range(m):
        s=0
        for x in map(int, input().split()):
            s +=x
            temps.append((s,i))
temps.sort()

penalitzacio=[0]*m
k=0
i=0
while i <len(temps):
    j=i
    