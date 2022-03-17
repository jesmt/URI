primeiro = -1
anterior = primeiro
soma = 0
n = int(input())

for i in range(n):
    t = int(input())
    if (anterior!= primeiro) and (t - anterior < 10):
        soma -= 10 - (t - anterior)
    anterior = t
    soma += 10

print(soma)