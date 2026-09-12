def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime = list()
for i in range(2, 1121):
    if is_prime(i):
        prime.append(i)

dp = list()
for _ in range(15):
    dp.append([0] * 1121)

dp[0][0] = 1
for p in prime:
    for j in range(14, 0, -1):
        for s in range(1120, p - 1, -1):
            dp[j][s] += dp[j - 1][s - p]

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    print(dp[k][n])