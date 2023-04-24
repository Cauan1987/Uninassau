tabelaprecos = { 
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00, 
    5: 1.50,}
codigo = int(input('Qual o código do item: '))
quantidade = int(input('Quantos itens tem: '))
if codigo not in tabelaprecos:
    print("Código inválido!")
else:
    precounitario = tabelaprecos[codigo]
    valortotal = precounitario * quantidade

    # exibe o resultado na tela
    print("Total: R$ {:.2f}".format(valortotal))
    

