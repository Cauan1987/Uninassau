n1 = float(input('Quanto o aluno tirou na n1: '))
n2 = float(input('Quanto o aluno tirou na n2: '))
n3 = float(input('Quanto o aluno tirou na n3: '))
n4 = float(input('Quanto o aluno tirou na n4: '))
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    notaexame = float(input('Qual a nota da recuperação: '))
    print("Nota do exame: {:.1f}".format(notaexame))
    mediafinal = (media + notaexame) / 2
    if mediafinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(mediafinal))


