def compare(prev_num, num, prev, next):
    if prev_num == '0':
        num1 = num[prev]+num[next]
        num2 = num[next]+num[prev]
    else:
        num1 = prev_num+num[next]
        num2 = num[next]+prev_num

    num1 = int(num1)
    num2 = int(num2)

    if(num1 > num2):
        num1 = str(num1)
        return compare(num1, num, prev+2, next+2)
    else:
        num2 = str(num2)
        return compare(num2, num, prev+2, next+2)




    
        


while True:
    n = int(input())
    if n==0:
        break
    num = list(input().split())
    new_num = compare('0', num, 0, 1)


    
