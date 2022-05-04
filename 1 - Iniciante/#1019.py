# 1019

# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# ler um valor inteiro(segundos)
valor_segundos = int(input())

# calcular o valor segundos em horas, minutos e segundos
horas = (valor_segundos//3600)
segundos = (valor_segundos % 3600)
minutos = (segundos//60)
segundos = (segundos % 60)

# imprimir o tempo calculado no formato horas:minutos:segundos
print(str(horas)+":"+str(minutos)+":"+str(segundos))
