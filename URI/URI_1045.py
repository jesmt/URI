num = input()
x, y, z = (num.split())
x = float(x)
y = float(y)
z = float(z)

if x >= y and x >= z:
    A = x
    if y >= z:
        B = y
        C = z
    if z >= y:
        B = z
        C = y

if y >= x and y >= z:
    A = y
    if x >= z:
        B = x
        C = z
    if z >= x:
        B = z
        C = x
if z >= x and z > y:
    A = z
    if x >= y:
        B = x
        C = y
    if y >= x:
        B = y
        C = x

if A >= (B + C):
    print(f'NAO FORMA TRIANGULO')
else :
    if A**2 == B**2 + C**2:
        print(f'TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2:
        print(f'TRIANGULO OBTUSANGULO')
    if A**2 < B**2 + C**2:
        print(f'TRIANGULO ACUTANGULO')
    if A == B == C:
        print(f'TRIANGULO EQUILATERO')
    elif A == B or B == C or A == C:
        print(f'TRIANGULO ISOSCELES')
        