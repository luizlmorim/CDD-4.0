'''Faça um código para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas
vezes esse número aparece no vetor.'''
vetor = []

for i in range(10):
    vetor.append(float(input("Digite os valores aqui: ")))

x = float(input('Digite um número qualquer: '))

cont = 0
for y in range(10):
    if x == vetor[y]:
        cont=+1
print(cont)

