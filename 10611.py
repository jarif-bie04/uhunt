from bisect import *

N = int(input())
height_N = list(map(int, input().split()))
Q = int(input())
luchu_height = list(map(int, input().split()))

for i in luchu_height:
    index_left = bisect_left(height_N, i)
    if index_left == 0:
        small = 'X'
    else:
        small = height_N[index_left-1]

    index_right = bisect_right(height_N, i)
    if index_right == len(height_N):
        big = 'X'
    else:
        big = height_N[index_right]

    print(f"{small} {big}")