codigo1 = int(input("Digite o código da peça 1: "))
quantidade1 = int(input("Digite o número de peças 1: "))
valor1 = float(input("Digite o valor unitário da peça 1: "))
print()
codigo2 = int(input("Digite o código da peça 2: "))
quantidade2 = int(input("Digite o número de peças 2: "))
valor2 = float(input("Digite o valor unitário da peça 2: "))
print()
total = quantidade1 * valor1 + quantidade2 * valor2

print("O valor total a ser pago é R$ {:.2f}",format(total))
