#O programa ler as notas nota1 e nota2. Calcula e imprime a média desse aluno. Só aceita valores entre 0 e 10, para cada nota.
#Quando o valor é inválido, ele pede novamente.
print("\nVamos calcular sua média!")

resp = "s"
while resp == "s":
    n1 = float(input("\nDigite sua primeira nota:\t"))
    while n1 < 0 or n1 > 10: #caso a nota esteja fora do intervalo. OBS:
        n1 = float(input("\nnota inválida. Digite novamente:\t"))

    n2 = float(input("\nDigite sua segunda nota:\t"))
    while n2 < 0 or n2 > 10:
        n2 = float(input("\nnota inválida. Digite novamente:\t"))

    media = (n1+n2)/2
    print(media)
    resp = input('Deseja continuar? Sim(s)')





