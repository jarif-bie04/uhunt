T = int(input())
for case in range(T):
    n, P, Q = map(int, input().split())
    egg = list(map(int, input().split()))
    egg.sort()
    count = 0

    i = 0
    while i < n:
        if egg[i] <= Q and i < P:
            count += 1
            Q -= egg[i]
            i += 1
        else:
            break
        
    print(f"Case {case + 1}: {count}")