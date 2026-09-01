t = int(input())

for i in range(t):
    n = int(input())
    m  = list(map(int, input().split()))

    tall = 0
    small = 0

    for j in range(n-1):
        if m[j+1] - m[j] > 0:
            tall += 1
        elif m[j+1] - m[j] < 0:
            small += 1

    print(f"Case {i+1}: {tall} {small}")