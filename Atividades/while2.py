'''Faça um código que receba o número de alunos de uma sala de aula e depois solicite as notas desses alunos, no final, mostre a
média aritmética da turma.'''

x=1
soma= 0
alunos = int(input("Informe a quantidade de alunos: "))  #descobrindo a quantidade de alunos - quantidade de vezes que o while vai rodar
while x<= alunos: #enquato x for menor a quantidade de alunos o while será executado OBS: criar a saída do while x+=1
    nota = float(input("Digite as notas do alunos: "))
    soma = soma+nota #soma+=nota
    x+=1 #x=x+1
media = soma/alunos
print(media)