n = int(input("Digite um valor entre 1 e 10: "))
if n < 1 or n > 10:
    print("Valor inválido. O valor deve estar entre 1 e 10.")
else:
    for i in range(11):
        print("{} x {} = {}".format(i, n, i*n))
        
