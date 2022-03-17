while True:
    n = int(input())

    if n == 0:
        break

    xd, yd = input().split()
    xd, yd = int(xd), int(yd)

    for i in range(n):
        x, y = input().split()
        x, y = int(x), int(y)

        if x > xd and y > yd:
            print("NE")
        elif (x == xd) or (y == yd):
            print("divisa")
        elif x < xd and y > yd:
            print("NO")
        elif x < xd and y < yd:
            print("SO")
        elif x > xd and y < yd:
            print("SE")
