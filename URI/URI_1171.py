n = int(input())
lista = {}
for i in range(n):
    valor = int(input())
    if valor in lista:
        lista[valor] += 1
    else:
        lista[valor] = 1

chave = lista.keys()
chave = sorted(chave)

for i in chave:
    print(f"{i} aparece {lista[i]} vez(es)")