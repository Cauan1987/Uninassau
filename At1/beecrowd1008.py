numero = int(input('Qual o número do funcionário: '))
hora = float(input('Quantas horas ele trabalha: '))
valor = float(input('Quanto o funcionário recebe por hora: '))
salario = hora * valor
print('O número do funcionário é {} e ele recebe R${:.2f}'.format(numero, salario))


