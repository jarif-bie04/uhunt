while True:
    try:
        x, y = map(int, input().split())
        s = abs(y - x)
        print(s)
    except EOFError:
        break