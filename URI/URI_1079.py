n = int(input())
for i in range(n):
    a, b, c = input().split()
    a, b, c = float(a), float(b), float(c)
    media = (2 * a + 3 * b + 5 * c) / 10
    print(f'{media:.2}')