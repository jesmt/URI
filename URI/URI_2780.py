distance = float(input())
if distance <= 800:
    x = 1
elif 800 < distance <= 1400:
    x = 2
else:
    x = 3
print(int(x))
