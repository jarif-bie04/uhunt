t = int(input())
for i in range(t):
    n = input().strip()
    count = 0
    k = 0
    for j in n:
        if j != 'X':
            k += 1
            count += k
        else:
            k = 0
    print(f"{count}")
