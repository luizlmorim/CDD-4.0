'''Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente,
após completar a digitação, imprimir , nome, senha e posição dos dados no array'''

usuarios = []
senhas = []

for u in range(5):
    usuarios.append(input("Informe seu nome de usuário: "))
    senhas.append(input("Digite sua senha: "))
for x in range(5):
    print("Usuário: ", usuarios[x], "\nSenha: ", senhas[x], "\nPosição: ", x)

#mostrar só o índice usa-se a apenas a variável, no caso, "x"
#mostrar os itens na lista 'nome_da_lista[índice]'
