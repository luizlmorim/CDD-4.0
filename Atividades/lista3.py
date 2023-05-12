lista_alunos = []
n = int(input("Digite a quantidade de alunos: "))
for a in range(n): #o range vai repitir a quandidade de alunos
    lista_alunos.append(input("Digite o nome do aluno: "))
for a in range(n):
    print(a, lista_alunos[a])

pesquisa = input("Pesquise o aluno aqui: ")
cont = 0
for p in range(n): #preciamos abrir um outro for para pecorrer o array
    if pesquisa == lista_alunos[p]: #abrimos um if para comparar se o item pesquisado existe dentra lista.
        print(p, lista_alunos[p]) #usamos as chaves para demilita a posição(o índice) dos iens(alunos)
    else:
        cont+=1 #contador criado para não ficar repitindo "não encontrado" várias vezes.
if cont == n:
    print("não encontardo")


