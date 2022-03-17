# -*- coding: utf-8 -*-
while True:
    n, m = input().split()
    n, m = int(n), int(m)

    if n == m == 0:
        break

    linha = []
    for i in range(n):
        linha.append(input())

    a, b = input().split()
    a, b = int(int(a)/n), int(int(b)/m)

    redimensionado = []

    for i in linha:
        nova_linha = ''
        for j in i: # trata elementos da coluna
            nova_linha += j * b

        for j in range(a): # add a nova linha tratada 'a' vezes na nova lista
            redimensionado.append(nova_linha)

    for i in redimensionado: # imprime intem a item da lista redimensionada
        print(i)
    print()










