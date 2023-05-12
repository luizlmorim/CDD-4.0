pin = "luiz123"
senha = input("Digite sua senha: ")
tentantivas = 0

while tentantivas <3:
    senha = input("Digite sua senha: ")
    if senha == pin:
        print("Acesso Liberado")
        break
    else:
        tentantivas +=1
        if tentantivas <3:
            print("Senha incorreta. Tente novamente")
        else:
            print("Senha bloqueada")
