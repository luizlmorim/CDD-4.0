'''Faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido, caso o segundo valor digitado,
 seja zero, solicite novamente o valor, informando que só aceitaremos valores diferentes de zero.'''

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
resultado=0

while num2==0:
    print("só permitimos num2 diferente de Zero")
    n2=float(input())
else:
    resultado=n1/n2
    print(resultado)