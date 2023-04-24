somapares = 0
somageral = 0
quantidadepares = 0
quantidadegeral = 0

while True:
    numero = int(input("Digite um número positivo (ou 0 para encerrar): "))
    if numero == 0:
        break
    elif numero > 0:
        somageral += numero
        quantidadegeral += 1
        if numero % 2 == 0:
            somapares += numero
            quantidadepares += 1

if quantidadegeral == 0:
    print("Nenhum número válido foi digitado.")
else:
    mediageral = somageral / quantidadegeral
    print("Média geral: %.2f" % mediageral)
    print("Quantidade de números pares: %d" % quantidadepares)
    if quantidadepares == 0:
        print("Não foi possível calcular a média dos valores pares.")
    else:
        mediapares = somapares / quantidadepares
        print("Média dos valores pares: %.2f" % mediapares)
        


