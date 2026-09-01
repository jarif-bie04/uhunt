while True:
    try:
        N, B, H, W = map(int,input().split())
        price_list = list()
        
        for _ in range(H):
            p = int(input())
            a = list(map(int, input().split()))

            for i in range(len(a)):
                if(a[i] >= N):
                    total = N * p
                    price_list.append(total)

        price_list = sorted(price_list)

        if(price_list) and price_list[0]<=B:
            print(price_list[0])
        else:
            print("stay home")

    except EOFError:
        break
