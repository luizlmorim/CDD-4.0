'''Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor.A seguir, o algoritmo deverá informar
(1) todos os números pares que existem no vetor; (2) o menor e o maior valor existente no vetor; (3) quantos dos valores do vetor são
maiores que a média desses valores:'''
vetor = []

for i in range(10):
    vetor.append(int(input("Digite os números aqui: ")))
for y in range(10):
    if vetor[y] % 2 == 0:
        print('par: ', vetor[y])
    else:
        print('impar: ', vetor[y])

maior = vetor[0]
for u in range(10):
    if vetor[u] > maior:
        maior = vetor[u]
print("maior valor: ", maior)

soma = 0
cont=0
for z in range(10):
    soma = soma + vetor[z]
media = soma/10

for k in range(10):
    if vetor[k] > media:
        cont+=1
print("Quantidade de valores maiores que a média: ", cont)

