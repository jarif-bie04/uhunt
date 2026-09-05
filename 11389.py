while True:
    n, d, r = map(int, input().split())
    if n == 0 and d == 0 and r == 0:
        break
    morning = list()
    night = list()
    x = list(map(int, input().split()))
    for i in range(n):
        morning.append(x[i])
    y = list(map(int, input().split()))
    for i in range(n):
        night.append(y[i])
    morning.sort()
    night.sort(reverse=True)
    total = 0
    for i in range(n):
        if morning[i] + night[i] > d:
            total += (morning[i] + night[i] - d) * r
    print(total)