while True:
    h, m = map(int, input().split(":"))

    if h == 0 and m == 00:
        break
    angle = abs(((60 * h) - (11 * m))/2)

    if angle > 180:
        print(f"{360 - angle:.3f}")
    else:
        print(f"{angle:.3f}")