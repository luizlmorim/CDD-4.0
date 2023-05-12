a = []
m = []

for i in range(10):
    a.append(int(input("Digite os números aqui: ")))

x = int(input('Digite o novo numero aqui: ')) #amazena o mulplicador

for b in range(10):
    m.append(a[b]*x)

print(a, x, m)

