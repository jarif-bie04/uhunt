t = int(input())
for i in range(t):
    num = list(map(int, input().split()))
    num.pop(0)
    largest = max(num)
    print(f"Case {i+1}: {largest}")