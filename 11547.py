n = int(input())
for i in range(n):
    num = int(input())
    result = (((num*567)/9)+7492)*235/47-498
    final_result = abs(int(result)) % 100
    final_result /= 10
    print((int(final_result)))