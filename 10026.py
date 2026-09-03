t = int(input())

for _ in range(t):
    blank = input()
    N = int(input())
    task = list()
    for i in range(N):
        line = input().split()
        task.append((int(line[0]), int(line[1]), i))

    task.sort(key=lambda x: x[1]/x[0], reverse=True)

    print(" ".join(str(x[2]+1) for x in task))

    if _ < t-1:
        print()