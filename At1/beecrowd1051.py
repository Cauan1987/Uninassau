salario = float(input('Qual o salário: '))

if salario <= 2000.00:
    print("Isento")
elif salario <= 3000.00:
    imposto = (salario - 2000.00) * 0.08
    print("R$ {:.2f}".format(imposto))
elif salario <= 4500.00:
    imposto = 1000.00 * 0.08 + (salario - 3000.00) * 0.18
    print("R$ {:.2f}".format(imposto))
else:
    imposto = 1000.00 * 0.08 + 1500.00 * 0.18 + (salario - 4500.00) * 0.28
    print("R$ {:.2f}".format(imposto))
