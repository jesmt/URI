import math

while True:
    try:
        N = int(input())
        H, C, L = input().split()
        H, C, L = int(H), int(C), int(L)

        area = (L * (math.sqrt((C ** 2) + (H ** 2))) * N) / 10000

        print("%.4f" % area)

    except EOFError:
        break