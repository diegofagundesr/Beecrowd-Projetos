# beecrowd | 1015

# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles

# ler quatros valores x1, y1, x2 e y2
p1 = input().split()
x1 = float(p1[0])
y1 = float(p1[1])

p2 = input().split()
x2 = float(p2[0])
y2 = float(p2[1])

# calcular o valor da distancia dos pontos segundo a fórmula cedida

distancia = ((x2-x1)**(2) + (y2-y1)**(2))**(1/2)

print('{:.4f}'.format(distancia))
