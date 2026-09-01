t = int(input())
for i in range(t):
    l, w, h = map(int, input().split())
    if l <= 20 and w <= 20 and h <= 20:
        print(f"Case {i+1}: good")
    else:
        print(f"Case {i+1}: bad")
