T = int(input())
for _ in range(T):
    n = int(input())
    coin_value = list(map(int, input().split()))

    coin_count = 2
    sum = coin_value[0]
    for i in range(1, n-1):
        if sum + coin_value[i] < coin_value[i+1]:
            coin_count += 1
            sum += coin_value[i]
    if len(set(coin_value)) == 1:
        print(1)
    else:
        print(coin_count)
