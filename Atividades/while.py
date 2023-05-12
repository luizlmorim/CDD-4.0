#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.(usando While)

'''while <expr>
        <statementes'''
x=1 #variável de controle-contador
soma = 0 #contador soma incia com 0
while x<=10: #expressão - condicional
    num=float(input("informe o número")) #declarando a variável dentro do while - recebendo o número
    soma = soma+num #contador - somando os valores do usuário
    x =x+1 #condição para a saída - x está sendo somando com mais +1 até chegar em 11 (no caso um valor maior do que 10)
media = soma/10
print(media)