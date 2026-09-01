t = int(input())
x = 0
for _ in range(t):
    n, k, p = map(int, input().split())
    i = k
    for _ in range(p):
        if i<n:
            i+=1
        elif i>n:
            i=1
            i+=1
        elif i==n:
            i=1
    print(f"Case {x+1}: {i}")
    x+=1
    