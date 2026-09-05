while True:
    try:
        s, t = input().split()
        if s in t:
            print("Yes")
        else:
            i = 0
            j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            if i == len(s):
                print("Yes")
            else:
                print("No")

    except EOFError:
        break