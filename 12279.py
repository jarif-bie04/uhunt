j = 0
while True:
    try:
        n = int(input())
        count_total = 0
        count_nonZero = 0
        count_zero = 0

        num = list(map(int, input().split()))

        for i in num:
            if i != 0:
                count_nonZero += 1
            else:
                count_zero += 1

        count_total = count_nonZero - count_zero
        if n != 0:
            print(f"Case {j+1}: {count_total}")
            j += 1

    except EOFError:
        break