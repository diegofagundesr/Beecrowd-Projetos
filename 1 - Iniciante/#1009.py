#beecrowd | 1009

# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas

# ler o nome do vendedor, seu salário fixo e o total de vendas

nome_vendedor = input()
salario_vendedor = float(input())
total_de_vendas = float(input())

# calcular o salario total, salário somado a comissão de 15%
salario_total = salario_vendedor + (total_de_vendas*(0.15))

# imprimir o salario total
print("TOTAL = R$", '{:.2f}'.format(salario_total))
