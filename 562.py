def dividingCoins(coin, midSum):    
    dp = list()
    dp = [[0] * (midSum+1) for _ in range(len(coin)+1)]
    for i in range(len(coin)+1):
        dp[i][0] = 1
    for i in range(1, len(coin)+1):
        for j in range(1, midSum+1):
            dp[i][j] = dp[i - 1][j]
            if j >= coin[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - coin[i - 1]]
    for j in range(midSum, -1, -1):
        if dp[len(coin)][j]:
            return j
    return 0


t = int(input())
for _ in range(t):
    m = int(input())
    coin = list(map(int, input().split()))
    coinSum = sum(coin)
    midSum = coinSum//2
    per1 = dividingCoins(coin, midSum)
    per2 = coinSum - per1
    print(abs(per1 - per2))