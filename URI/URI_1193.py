n = int(input())

for i in range(n):

    num, tipo = input().split()

    print(f"Case {i+1}:")

    if tipo == 'dec':
        # dec to hex
        a = int(num)
        hexa = hex(a)
        print(hexa[2::], "hex")

        # dec to bin
        a = int(num)
        a = bin(a)
        print(a[2::], "bin")

    elif tipo == 'hex':
        # hex to dec
        deci = int(num, 16)
        print(deci, "dec")

        #hex to bin
        a = int(deci)
        a = bin(a)
        print(a[2::], "bin")



    else:
        # bin to dec
        deci = int(num, 2)
        print(deci, "dec")

        # bin to hex
        hexa = hex(deci)
        print(hexa[2::], "hex")


    print()
