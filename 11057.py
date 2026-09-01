# fin = open("input.txt", "r")
# fout = open("output.txt", "w")

while True:
    try:
        n = int(input())
        price = list(map(int, input().split()))
        m = int(input().strip())
        line4 = input()

        price = sorted(price)

        low = 0
        high = len(price) - 1

        i = low
        j = high

        n1 = 0
        n2 = 0
            
        while(i<j):
            total = price[i]+price[j]

            if(total == m):
                n1 = i
                n2 = j
                i+=1
                j-=1

            elif(total < m):
                i+=1
            else:
                j-=1

        # fout.write(f"Peter should buy books whoseprices are {price[n1]} and {price[n2]}\n\n")
        print(f"Peter should buy books whose prices are {price[n1]} and {price[n2]}.")
        print()

    except EOFError: 
        break

# fin.close()
# fout.close()
