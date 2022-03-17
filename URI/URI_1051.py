salario = float(input())

if salario <= 2000.00:
    i = 0
    print('Isento')

elif 2000.00 < salario <= 3000.00:
    i = (salario - 2000.00) * (8 / 100)

if 3000.00 < salario <= 4500.00:
    i = ( salario - 3000.00) * (18 / 100) + ((8 / 100) * (1000.00))

if salario > 4500.00:
    i = ((18 / 100) * (1500.00)) + ((8 / 100) * (1000.00)) + (salario - 4500.00) * (28 / 100)

if salario > 2000.00:
    i = float(i)
    print('R$ {:.2f}'.format(i))