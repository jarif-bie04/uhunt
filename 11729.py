inc = 0
while True:
    N = int(input())

    if N == 0:
        break

    S = list()
    
    for i in range(N):
        b, j = map(int, input().split())
        S.append((b, j))

    S.sort(key=lambda x: x[1], reverse=True)
    count = 0
    res_count = 0

    for b, j in S:
        count += b
        res_count = max(res_count, count+j)

    print(f"Case {inc + 1}: {res_count}")
    inc += 1
