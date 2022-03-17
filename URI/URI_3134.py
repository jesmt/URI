# -*- coding: utf-8 -*-
valor_a, resto_a = input().split('.')
valor_a = int(valor_a)*10 + int(resto_a)
valor_b, resto_b = input().split('.')
valor_b = int(valor_b) * 10 + int(resto_b)
valor_c, resto_c = input().split('.')
valor_c = int(valor_c) * 10 + int(resto_c)
valor_d, resto_d = input().split('.')
valor_d = int(valor_d) * 10 + int(resto_d)

if valor_a == valor_b + valor_c + valor_d:
    print("YES")
elif valor_b == valor_a + valor_c + valor_d:
    print("YES")
elif valor_c == valor_a+ valor_b + valor_d:
    print("YES")
elif valor_d == valor_a + valor_b + valor_c:
    print("YES")
elif valor_a + valor_b == valor_c + valor_d:
    print("YES")
elif valor_a + valor_c == valor_b + valor_d:
    print("YES")
elif valor_a + valor_d == valor_b + valor_c:
    print("YES")
else:
    print("NO")