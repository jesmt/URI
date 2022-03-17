n = int(input())
lista = []

for i in range(n):
    lista.append(input())

for i in range(n):
    count = 0
    s = lista[i]
    for j in range(len(s)):
        if "!" in s[j]:
            count += 1
    K = count
    N = int(s[0:(len(s) - K)]) #da posição zero ate a posição antes de começar as exclamações
    result = 1
    for z in range(N , 1, -K):
        # print(f"Z: {z} / N: {N} / K: {K}")
        #print(f"{result} = {result} *  {z}")
        #print(z)
        result = result * z
    print(result)
