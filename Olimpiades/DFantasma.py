n = int(input())

for i in range(n):
    s = input()
    x = s.split()
    l = []
    normal = True

    for e in x:
        num = int(e)

        if num == 0:
            continue
        elif num > 0:
            l.append(num)
        else:
            if not l or l[-1] != -num:
                normal = False
                break
            l.pop()

    if l:
        normal = False

    if normal:
        print("NORMAL")
    else:
        print("PARANORMAL")
