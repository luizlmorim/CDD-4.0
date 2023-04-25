lista_alunos = []
n = int(input("Digite a quantidade de alunos: "))
for a in range(n):
    lista_alunos.append(input("Digite o nome do aluno: "))
for a in range(a): #usamos um novo for para pecorrer a lista e imprimir cada item, não a lisat em si.
     print(a, lista_alunos[a])

'''Ateração - mostarndo o indice e o item'''
lista_alunos = []
n = int(input("Digite a quantidade de alunos: "))
for a in range(n):
    lista_alunos.append(input("Digite o nome do aluno: "))
for a in range(n): #usamos um novo for para pecorrer a lista e imprimir cada item, não a lisat em si.
     print(a, lista_alunos[a]) #mostrando o nome e o índice. a se referindo ao indice
