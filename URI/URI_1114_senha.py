x = 2002
senha = int(input())
while True:
    if senha == x:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
        senha = int(input())

