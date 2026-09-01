count = 0

while True:
    try:
        line = input()
        for i in line:
            if i == '"':
                count = count + 1
                if count % 2 == 1:
                    print("``", end="")
                    continue
                else:
                    print("''", end="")
                    continue
            print(i, end="")
        print()
    except EOFError:
        break
# "To be or not to be," quoth the Bard, "that is the question".
# The programming contestant replied: "I must disagree. To `C' or not to `C', that is The Question!"