while True:
    try:
        num = int(input())
        a = 1
        c = 1
        while a % int(num) != 0:
            a = (10 * a + 1) % int(num)
            c += 1
        print(c)
    except EOFError:
        break