# 1017

# Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários.

# ler o tempo gasto em horas na viagem e a VM durante a viagem.
tempo = int(input())
vm = int(input())

# calcular  litros necessários para realizar a viagem
distancia = vm * tempo
litros = distancia/12

# imprimir a quantidade de litros necessária para realizar a viagem
print('{:.3f}'.format(litros))
