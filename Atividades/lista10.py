'''Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um
por linha.'''

nomes = []
for z in range(5):
    nomes.append(input("Digite os nomes aqui: "))
print(nomes)
for i in range(4,-1,-1): #ordem inversa
    print(nomes[i], end=" ")