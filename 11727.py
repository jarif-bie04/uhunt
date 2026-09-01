n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    if (x > y and x < z) or (x < y and x > z):
        print(f"Case {i + 1}: {x}")
    elif (y > x and y < z) or (y < x and y > z):
        print(f"Case {i + 1}: {y}")
    else:
        print(f"Case {i + 1}: {z}")