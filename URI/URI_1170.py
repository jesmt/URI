lista = []
i = 0
count = 0
while i < n:
    lista.append(float(input()))
    i +=1
i = 0

while i < n:
    lista[i] = lista[i]/2
    count += 1
    if lista[i] <= 1:
        print(count, "dias")
        i = i + 1
        count = 0




