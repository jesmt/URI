while True:
    try:
        num = int(input())
        for i in range(1, num + 1, 2):
            print((num - i) // 2 * ' ', end='')
            print('*' * i)

        print(num // 2 * ' ', end='')
        print('*')
        print(((num // 2) - 1) * ' ', end='')
        print('***')
        print()

    except EOFError:
        break