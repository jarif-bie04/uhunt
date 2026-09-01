test_case = int(input())

for t in range(test_case):
    blank = input()    
    height = int(input())
    wave = int(input())
    for k in range(wave):
        for i in range(1, height+1):
            for j in range(i):
                print(i, end='')
            print()

        
        for i in range(height-1, 0, -1):
            for j in range(i):
                print(i, end='')
            print()
        if k != wave - 1:
            print()

    if t != test_case - 1:
        print()