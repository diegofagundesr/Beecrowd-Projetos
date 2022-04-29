#beecrowd | 1008

# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário.

# ler o numero do funcionário, numero de horas trabalhadas e o valor que recebe por hora
n_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

# calcular o salario
salario = (valor_hora * horas_trabalhadas)

# imprimir o numero e o salario do funcionario

print("NUMBER =", n_funcionario)
print("SALARY = U$", '{:.2f}' .format(salario))
