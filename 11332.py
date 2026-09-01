def sum_of_digits(n):
    sum = 0
    for i in range(len(n)):
        sum = int(n[i])+sum
    if len(n) == 1:
        return sum
    else:
        return sum_of_digits(str(sum))
    

while True:
    x = input()
    if x == '0':
        break
    if len(x) == 1:
        print(x)
    else:
        print(sum_of_digits(x))