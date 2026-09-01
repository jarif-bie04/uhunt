while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if n > m:
        head = list()
        for _ in range(n):
            head.append(int(input()))
            head.sort()
            knight = list()
        for _ in range(m):
            knight.append(int(input()))
        knight.sort()
        print("Loowater is doomed!")
    else:
        head = list()
        for _ in range(n):
            head.append(int(input()))
        head.sort()
        knight = list()
        for _ in range(m):
            knight.append(int(input()))
        knight.sort()
        total_cost = 0
        i = 0
        j = 0
        while i < n and j < m:
            if head[i] <= knight[j]:
                total_cost += knight[j]
                i += 1
            j += 1

        print(total_cost if i == n else "Loowater is doomed!")