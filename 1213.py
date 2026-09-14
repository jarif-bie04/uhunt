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

tab = list()
for _ in range(15):
    tab.append([0] * 1121)

tab[0][0] = 1
for p in prime:
    for k in range(14, 0, -1):
        for n in range(1120, p - 1, -1):
            tab[k][n] += tab[k - 1][n - p]

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    print(tab[k][n])