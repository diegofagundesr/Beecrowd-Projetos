# beecrowd | 1011

# Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3

# ler o raio fornecido
raio = float(input())

# fórmula e pi
pi = 3.14159
volume = ((4/3) * pi * raio**3)

# imprimir resultado do calculo com a mensagem VOLUME
print("VOLUME =", '{:.3f}'.format(volume))
