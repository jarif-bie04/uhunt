import heapq

while True:
    N = int(input())
    if N == 0:
        break
    num = list(map(int, input().split()))
    heapq.heapify(num)
    total_cost = 0
    while len(num) > 1:
        x = heapq.heappop(num)
        y = heapq.heappop(num)
        total_cost += x + y
        heapq.heappush(num, x + y)

    print(total_cost)