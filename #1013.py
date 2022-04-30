# 1013

# Faça um programa que leia três valores e apresente o maior dos três valores lidos

# ler três valores
valores = input().split()
valor1 = int(valores[0])
valor2 = int(valores[1])
valor3 = int(valores[2])

# imprimir o maior dos três valores
print(max(valor1, valor2, valor3), "eh o maior")
