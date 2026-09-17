t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    street = n[1:]
    street.sort()
    mid = len(street) // 2
    dis = list()
    for i in range(len(street)):
        if street[mid] - street[i] != 0:
            dis.append(abs(street[mid] - street[i]))
    res = sum(dis)
    print(f"{res}")        