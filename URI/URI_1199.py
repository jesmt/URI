while True:
    n = input()
    if n[0] == '0': #hex to dec
        a = n[2::]
        deci = int(a, 16)
        print(deci)

    elif n[0] != 0:
        if int(n) < 0:
            break
        else: #dec to hex
            a = int(n)
            hexa = hex(a)
            print('0x', end="")
            print(hexa[2::].upper())