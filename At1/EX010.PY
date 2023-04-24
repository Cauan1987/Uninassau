A = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1
for i in range(A, 0, -1):
    print(i, end="")
    if i > 1:
        print(" X ", end="")
    else:
        print(" = ", end="")
    fatorial *= i
print(fatorial)

