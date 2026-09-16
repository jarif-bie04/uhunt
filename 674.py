coin = [1, 5, 10, 25, 50]

r = len(coin)
c = 7489

dp = [[0] * (c + 1) for _ in range(r)]

for i in range(r):
    dp[i][0] = 1

for j in range(c + 1):
    dp[0][j] = 1

for i in range(1, r):
    for j in range(1, c + 1):
        if coin[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - coin[i]]

while True:
    try:
        n = int(input())
        print(dp[r - 1][n])
    except EOFError:
        break