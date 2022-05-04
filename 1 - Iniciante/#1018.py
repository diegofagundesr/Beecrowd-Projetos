# 1018

# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.

# ler um valor inteiro
valor = int(input())

# decompor o valor cedido em notas de 100, 50, 20, 10, 5, 2 e 1.

# 100
notas100 = valor//100
resto = valor % 100

# 50
notas50 = resto//50
resto = resto % 50

# 20
notas20 = resto//20
resto = resto % 20

# 10
notas10 = resto//10
resto = resto % 10

# 5
notas5 = resto//5
resto = resto % 5

# 2
notas2 = resto//2
notas1 = resto % 2

# imprimir o resultado
print(valor)
print(notas100, "nota(s) de R$ 100,00")
print(notas50, "nota(s) de R$ 50,00")
print(notas20, "nota(s) de R$ 20,00")
print(notas10, "nota(s) de R$ 10,00")
print(notas5, "nota(s) de R$ 5,00")
print(notas2, "nota(s) de R$ 2,00")
print(notas1, "nota(s) de R$ 1,00")
