A = float(input('Qual o valor de a: '))
B = float(input('Qual o valor de b: '))
C = float(input('Qual o valor de c: '))

if A + B > C and A + C > B and B + C > A:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((A + B) * C) / 2
    print(f"Area = {area:.1f}")
    


