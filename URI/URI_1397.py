while True:
    n = input()
    if n == '0':
        break
    pontos_og = 0
    pontos_fi = 0
    for i in range(int(n)):
        og, fi = input().split()
        og, fi = int(og), int(fi)
        if og > fi:
            pontos_og += 1
        elif fi > og:
            pontos_fi += 1

    print(pontos_og, pontos_fi)



