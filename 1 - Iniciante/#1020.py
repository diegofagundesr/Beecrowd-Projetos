# 1020

# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# ler a entrada em dias
idade = int(input())

# transformar o valor cedido em anos, meses e dias
anos = (idade//365)
resto = (idade % 365)

meses = (resto//30)
dias = (resto % 30)

# imprimir o valor transformado em anos, meses e dias
print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")
