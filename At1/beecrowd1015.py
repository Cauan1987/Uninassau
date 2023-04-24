x1, y1 = map(float, input('Digite as coordenadas do primeiro ponto (x1 y1): ').split())
x2, y2 = map(float, input('Digite as coordenadas do segundo ponto (x2 y2): ').split())
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('A distância entre os pontos é {:.4f}'.format(distancia))

