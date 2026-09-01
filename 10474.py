def binSearch(low, high, key):
    if low > high:
        return -1
    mid = low+(high-low)//2
    if low == high:
        if number[low] == key:
            return low
        else:
            return -1
    else:
        if number[mid] < key:
            return binSearch(mid + 1, high, key)
        elif number[mid] == key:
            if mid == 0 or number[mid-1]!=key:
                return mid
            else:
                return binSearch(low, mid-1, key)
        else:
            return binSearch(low, mid-1, key)

k = 0    
while True:
    size, no_keys = map(int, input().split())
    if size == 0 and no_keys == 0:
        break
    global number
    number = list()
    for _ in range(size):
        x = int(input())
        number.append(x)

    target = list()
    for _ in range(no_keys):
        y = int(input())
        target.append(y)

    number = sorted(number)
    # print(number)
    
    print(f"CASE# {k+1}:")
    for i in range(len(target)):
        pos = binSearch(0, len(number)-1, target[i])
        if pos != -1:
            print(f"{target[i]} found at {pos+1}")
        else:
            print(f"{target[i]} not found")

    k+=1