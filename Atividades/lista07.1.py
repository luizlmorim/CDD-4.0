usuarios = []
senhas = []

for u in range(5):
    usuarios.append(input("Informe seu nome de usuário: "))
    senhas.append(input("Digite sua senha: "))

login = input("Pesquise seu nome de usuário: ")
password = input("Confirme sua senha: ")

cont=0
for x in range(5):
    if login == usuarios[x] and password == senhas[x]:
        print("Login efetuado com sucesso!")
        break
    else:
         cont+=1 #aplicamos o contador para não repitir 5 vezes, usamos no caso cont como sinalizador.

if cont==5:
    print("Error! Login ou senha inválidas! ")


