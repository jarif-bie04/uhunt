while True:
    t = int(input())
    if t == 0:
        break
    else:
        x, y = map(int, input().split())
        for i in range(t):
            m, n = map(int, input().split())
            if (m == x and n == y) or (n == y) or (m == x):
                print("divisa")
            elif m > x and n > y:
                print("NE")
            elif m < x and n > y:
                print("NO")
            elif m < x and n < y:
                print("SO")
            else:
                print("SE")
            
