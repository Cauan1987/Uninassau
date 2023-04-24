A = int(input("Digite o valor inicial: "))
R = int(input("Digite a razão: "))

PG = []
for i in range(10):
    PG.append(A * (R ** i))

print("Sequência em P.G.: ", PG)
