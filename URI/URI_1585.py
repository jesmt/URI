num = int(input())
i = 0
lista = []
while i < num:
    lista.append(input())
    i += 1
for i in range(num):
    a, b = lista[i].split()
    print((int(a) * int(b) // 2), 'cm2')
