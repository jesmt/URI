# -*- coding: utf-8 -*-
import string
a = list(string.ascii_uppercase)
letra = input()

for i in range(len(a)):
    if letra == a[i]:
        print(i+1)