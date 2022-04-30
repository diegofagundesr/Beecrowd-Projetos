# beecrowd | 1012

# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

# receber três valores A,B e C
valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

# calcular área das figuras
# area do triangulo
area_triangulo = (A * C) / 2

# area do círculo
pi = 3.14159
area_circulo = (pi * C**2)

# area do trapezio
area_trapezio = ((A + B) * C) / 2

# area do quadrado
area_quadrado = (B * B)

# area do retângulos
area_retangulo = (A * B)

# mostrar resultado dos calculos das areas da figuras correspondentes
print("TRIANGULO: "'{:.3f}'.format(area_triangulo))
print("CIRCULO: "'{:.3f}'.format(area_circulo))
print("TRAPEZIO: "'{:.3f}'.format(area_trapezio))
print("QUADRADO: "'{:.3f}'.format(area_quadrado))
print("RETANGULO: "'{:.3f}'.format(area_retangulo))
