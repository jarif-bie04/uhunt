def digit_sum(n):
    total = 0
    while n!=0:
        total += n % 10
        n //= 10
    return total

n = int(input())
query = list()
mx = 0

for _ in range (n):
    a, b = map(int, input().split())
    query.append((a, b))
    mx = max(mx, b)
    
is_prime = [True] * (mx+1)
is_prime[0] = False
is_prime[1] = False

# Sieve of Eratosthenes
for i in range(2, (mx//2)+1):
    if is_prime[i]:
        for j in range(i*i, mx + 1, i):
            is_prime[j] = False
            
prefix = [0] * (mx + 1)
for i in range(2, mx+1):
    prefix[i] = prefix[i - 1]
    if is_prime[i] and is_prime[digit_sum(i)]:
        prefix[i] += 1
        
for a, b in query:
    print(prefix[b] - prefix[a - 1])