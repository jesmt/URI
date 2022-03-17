while True:
    try:
        v, t = input().split()
        d = int(v) * 2 * int(t)
        print("%.f" %d)
    except EOFError:
        break