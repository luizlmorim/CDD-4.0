n = int(input('Digite o número 3: '))
for x in range(n+1): #para cada número que recebo vou repitir ele a quantidade de vezes dele mesmo

    for k in range(x+1): #x é o limite do for, no caso ele inicia com 0
        print(k, end="")#end deixa na horizonatal
    print(" ")