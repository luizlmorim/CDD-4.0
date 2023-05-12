'''Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B
(de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B
(respeitando as mesmas posições) e escrever o vetor Soma.'''
a = []
b = []
c = []
n = int(input("Digite o tamanho dos vetores: "))

for i in range(n):
    a.append(float(input("insira os valores aqui: ")))
    b.append(float(input("insira os valores aqui: ")))

for x in range(n):
    c.append(a[x] + b[x])
    
print(c)