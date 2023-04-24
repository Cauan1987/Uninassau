soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
print("A soma dos números ímpares múltiplos de três entre 1 e 500 é:", soma)

