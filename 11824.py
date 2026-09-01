n = int(input())
for i in range(n):
    price = list()
    while True:
        x = int(input())
        if x==0:
            break
        price.append(x)

    price.sort(reverse=True)
    size = len(price)
    total_price = 0

    for j in range(size):
        total = 2*pow(price[j],j+1)
        total_price += total

    if total_price > 5000000:
        print("Too expensive")
    else:
        print(f"{total_price}")
