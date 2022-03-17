# -*- coding: utf-8 -*-

idade_em_dias = int(input())
ano = int(idade_em_dias/365)
mes = int((idade_em_dias % 365)/30)
dia = int((idade_em_dias % 365) % 30)
print(int(ano), "ano(s)")
print(int(mes), "mes(es)")
print(int(dia), "dia(s)")