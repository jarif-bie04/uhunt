def lcs(seq, sub_seq):
    m = len(seq)
    n = len(sub_seq)

    dp = list()
    for i in range(m + 1):
        dp.append([0] * (n + 1))
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq[i - 1] == sub_seq[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

while True:
    try:
        seq = input()
        sub_seq = input()

        print(lcs(seq, sub_seq))

    except EOFError:
        break