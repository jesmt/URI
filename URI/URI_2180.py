peso =  int(input())

sum = 0
i = 0
while i < 10:  # esse loop soma os 10 proximos pesos primos
    lista=[]
    for j in range(1,peso+1):  # guarad os divisores do peso na lista
        if peso%j ==0:
            lista.append(j)

    if lista[0]==1 and lista[1]==peso:  # se a lista tiver so os dois divisores, 1 e peso, então peso é primo
        i += 1
        sum += peso  # armazena a soma em sum

    peso += 1

velocidade = sum

tempo = 60000000 / velocidade

print(velocidade, "km/h")
print(int(tempo),"h /", int(tempo/24), "d")

