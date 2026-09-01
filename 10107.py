num = list()
length = 0
while True:
    try:
        x = int(input())
        num.append(x)
        length += 1
        num.sort()
        mid = length//2
        median = 0
        if length%2==0:
            median = (num[mid]+num[mid-1])//2
        else:
            median = num[mid]
        print(median)

    except EOFError:
        break