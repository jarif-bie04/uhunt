def dna(seq, subSeq):
    m = int(len_x)
    n = int(len_y)

    dp = list()
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(n+1):
        dp[0][i] = i
    for j in range(m+1):
        dp[j][0] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq[i-1] == subSeq[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

    return dp[m][n]
        
while True:
    try:
        len_x, x = map(str, input().split())
        len_y, y = map(str, input().split())

        seq = list()
        subseq = list()
        for i in range(int(len_x)):
            seq.append(x[i])
        for i in range(int(len_y)):
            subseq.append(y[i])

        print(f"{dna(x, y)}")
    except EOFError:
        break