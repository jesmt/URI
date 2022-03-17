import math
lista = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        lista.append(x)

i=0
while i<len(lista):
    j = 1
    quad = 0
    while j<= lista[i]:
        quad += j**2
        j += 1
    print(quad)
    i += 1

