pi = 3.14159
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
print()
areatriangulo = A * C / 2
areacirculo = pi * C ** 2
areatrapezio = (A + B) * C / 2
areaquadrado = B ** 2
arearetangulo = A * B
print()
print("Área do triângulo retângulo: {:.2f}".format(areatriangulo))
print("Área do círculo: {:.2f}".format(areacirculo))
print("Área do trapézio: {:.2f}".format(areatrapezio))
print("Área do quadrado: {:.2f}".format(areaquadrado))
print("Área do retângulo: {:.2f}".format(arearetangulo))

