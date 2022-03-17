import math
teste = []
while True:
    try:
        teste.append(int(input()))
    except EOFError:  # ctrl + d
        break

for i in range(len(teste)):
    print(int(math.log(teste[i],2)))