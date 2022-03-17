from math import sqrt

while True:
    try:
        r1, x1, y1, r2, x2, y2 = input().split()
        r1, x1, y1, r2, x2, y2 = int(r1), int(x1), int(y1), int(r2), int(x2), int(y2)
        d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if d == r1 - r2 or d < r1 - r2 or (d == 0 and r1 > r2):
            print("RICO")
        else:
            print("MORTO")

    except EOFError:
        break