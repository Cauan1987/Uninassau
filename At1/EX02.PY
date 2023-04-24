menor = float("inf")
maior = float("inf")

for i in range(15):
    altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))
    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura

print("A menor altura do grupo é {:.2f} metros.".format(menor))
print("A maior altura do grupo é {:.2f} metros.".format(maior))

