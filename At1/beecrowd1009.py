nome = input("Digite o nome do vendedor: ")
salariofixo = float(input("Digite o salário fixo do vendedor: "))
totalvendas = float(input("Digite o total de vendas efetuadas pelo vendedor: "))
comissao = totalvendas * 0.15
salariofinal = salariofixo + comissao
print("O vendedor {} receberá um salário final de R$ {:.2f}".format(nome, salariofinal))



