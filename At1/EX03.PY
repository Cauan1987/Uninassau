numpositivos = 0
numnegativos = 0
soma = 0

while True:
    num = float(input("Digite um número (ou um valor negativo para sair): "))
    
    if num < 0:
        break

    soma += num
    if num > 0:
        numpositivos += 1
    else:
        numnegativos += 1
media = soma / (numpositivos + numnegativos)
percpositivos = (numpositivos / (numpositivos + numnegativos)) * 100
percnegativos = (numnegativos / (numpositivos + numnegativos)) * 100
print("Média aritmética: %.2f" % media)
print("Quantidade de valores positivos: %d" % numpositivos)
print("Quantidade de valores negativos: %d" % numnegativos)
print("Percentual de valores positivos: %.2f%%" % percpositivos)
print("Percentual de valores negativos: %.2f%%" % percnegativos)
