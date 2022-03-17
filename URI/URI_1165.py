q = int(input())
for i in range(q):
    n = int(input())
    lista=[]
    for i in range(1,n+1):
        if n%i ==0:
            lista.append(i)

    if lista[0]==1 and lista[1]==n:
        print(n, "eh primo")
    else:
        print(n, "nao eh primo")