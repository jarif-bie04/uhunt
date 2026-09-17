import string

i = 1

while True:
    try:
        s1 = input()
        s2 = input()
        count = 0

        if len(s1) == 0 or len(s2) == 0:
            print(f"{i}. Blank!")

        else:
            tt = str.maketrans(string.punctuation, " " * len(string.punctuation))
            s1 = s1.translate(tt)

            for j in s2:
                if (j in s1) and (j != ' '):
                    count += 1
            
        print(f"{i}. Length of longest match: {count}")

        i+=1

    except EOFError:
        break