coin = [0, 1, 2, 4, 10, 20, 40, 100, 200, 400, 1000, 2000]

r = len(coin) - 1
c = 6000

dp = [[0] * (c + 1) for _ in range(r + 1)]

for i in range(r + 1):
    dp[i][0] = 1

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if coin[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - coin[i]]

while True:
    n = input().strip()

    if n == "0.00":
        break

    dollars, cents = n.split('.')

    dollars = int(dollars)
    cents = int(cents)

    c = dollars * 20 + cents // 5

    print(f"{n:>6}{dp[r][c]:17d}")
