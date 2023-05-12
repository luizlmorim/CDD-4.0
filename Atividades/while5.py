pin = "luiz123"
senha = input("Digite sua senha: ")
tentantivas = 0

while senha != pin and tentantivas >=2:
    print("Senha incorreta. Tente novamente")
    senha = input()
    tentativas =tentativas + 1

    break