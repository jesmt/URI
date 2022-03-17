n = int(input())
sum = 0
for i in range(n):
    t, v = input().split()
    t, v = int(t), int(v)
    sum += t*v
print(sum)