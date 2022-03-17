sum = 0
count = 0
for i in range(6):
    n = float(input())
    if n >= 0:
        count += 1
        sum += n
print(count,'valores positivos')
print(f'{sum/count:.2}')