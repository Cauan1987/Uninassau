cont0_25 = cont26_50 = cont51_75 = cont76_100 = 0
while True:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    if num >= 0 and num <= 25:
        cont0_25 += 1
    elif num >= 26 and num <= 50:
        cont26_50 += 1
    elif num >= 51 and num <= 75:
        cont51_75 += 1
    elif num >= 76 and num <= 100:
        cont76_100 += 1

print(f"Quantidade de números no intervalo [0-25]: {cont0_25}")
print(f"Quantidade de números no intervalo [26-50]: {cont26_50}")
print(f"Quantidade de números no intervalo [51-75]: {cont51_75}")
print(f"Quantidade de números no intervalo [76-100]: {cont76_100}")

