line_1 = input()  # N e G , 1ª linha
x, y = line_1.split()
qnt_runas = int(x)  #
qnt_amizade = int(y)
lines = []

for i in range(qnt_runas):
    lines.append(input())  # Ri e Vi

qnt_runas_recitadas = input()  # X
lista_de_runas=[]
lista_de_runas.append(input())  # guarda as runas recitadas

count = 0

r1 = lista_de_runas[0]
runa = r1.split()

for i in range(int(qnt_runas_recitadas)):
    r = runa[i]
    for j in range(qnt_runas):
        r2 = lines[j]
        r2, v2 = r2.split()
        if r == r2:
            count = count + int(v2)

if count >= qnt_amizade:
    print(count)
    print("You shall pass!")
else:
    print(count)
    print("My precioooous")

