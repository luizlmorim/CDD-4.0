lista_notas = []
soma = 0
cont = 0

for i in range(5):
    lista_notas.append(float(input("Digite as notas do alunos: ")))

for y in range(5):
    soma = soma + lista_notas[y]
media = soma / 5


for x in range(5):
    if lista_notas[x] >=media:
        cont+=1

print(media)
print(cont)



