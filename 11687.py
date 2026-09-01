def digit(length, digit_count):
    count = 0
    if length == 1:
        return digit_count+1
    else:
        while length > 0:
            length //= 10
            count += 1
    digit_count += 1
    return digit(count, digit_count)



while True:
    x = input()
    if x == 'END':
        break
    elif x == '1':
        print(1)
    else:
        length = len(x)
        print(digit(length, 1))