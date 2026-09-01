while True:
    n = int(input())
    if n == -1:
        break
    else:
        wrong = 0
        guess = 0

        word_1 = set(input())
        word_2 = input()
        used = set()

        len_1 = len(word_1)

        for ch in word_2:
            if ch in used:
                continue
            used.add(ch)

            if ch not in word_1:
                wrong += 1
            else:
                guess += 1

            if wrong == 7 or guess == len_1:
                break

        if wrong == 7 and guess != len_1:
            print(f"Round {n}")
            print("You lose.")
        elif wrong < 7 and wrong >= 0 and guess != len_1:
            print(f"Round {n}")
            print("You chickened out.")
        else:
            print(f"Round {n}")
            print("You win.")
        


