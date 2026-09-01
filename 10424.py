def sum(n):
    total = 0
    if n > 9:
        while n>9:
            total = 0
            while n>0:
                total += n%10
                n //= 10
            n = total
    else:
        total = n
    
    return total

def count(name):
    total = 0
    for ch in name:
        if ch >= 'A' and ch <= 'Z':
            total += ord(ch) - ord('A') + 1
        else:
            total += 0

    return sum(total)

while True:
    try:
        name_1 = input().upper()
        name_2 = input().upper()

        count_1 = count(name_1)
        count_2 = count(name_2)

        small = min(count_1, count_2)
        large = max(count_1, count_2)

        res = small / large * 100

        print(f"{res:.2f} %")

    except EOFError:
        break