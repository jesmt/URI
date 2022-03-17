q = int(input())
entrada = []
for i in range(q):
    entrada.append(input())

for i in range(q):
    a, b = entrada[i].split(" ")
    x = len(a) - len(b)
    if a[x:] == b:
        print("encaixa")
    else:
        print("nao encaixa")


