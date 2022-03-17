import math
n = int(input())
for i in range(n):
    lines = int(input())
    sum = 0
    for i in range(lines):
        sum += 2**i
    print(sum)