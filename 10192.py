def lcs(seq, subSeq):
    m = len(seq)
    n = len(subSeq)

    dp = list()
    for i in range(m+1):
        dp.append([0]*(n+1))

    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq[i-1]==subSeq[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


i = 1
while True:
    seq = input()
    if seq.startswith("#"):
        break
    subSeq = input()
    print(f"Case #{i}: you can visit at most {lcs(seq, subSeq)} cities.")
    i += 1