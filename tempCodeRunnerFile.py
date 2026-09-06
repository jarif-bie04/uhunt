T = int(input())
for case in range(T):
    n, P, Q = map(int, input().split())
    egg = list(map(int, input().split()))
    egg.sort()
    count = 0

    i = 0
    while i < n - 1:
        if egg[i] + egg[i+1] <= Q and (i + (i+1)) < P:
            count += 2
            Q -= (egg[i] + egg[i+1])
            P -= 2
            i += 1
        else:
            i += 1
    if count == 0:
        i = 0
        while i < n:
            if egg[i] <= Q and i < P:
                count += 1
                Q -= egg[i]
                P -= 1
            i += 1
        
    print(f"Case {case + 1}: {count}")