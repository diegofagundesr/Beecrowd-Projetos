# beecrowd | 1014

# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros)

# ler distancia total fornecida e total de combustível gasto.
X = int(input())
Y = float(input())

# fazer cálculo do consumo médio do automóvel
consumo_medio = (X / Y)

# imprimir o resultado do cálculo, acompanhado de "km/l"
print('{:.3f}'.format(consumo_medio), "km/l")
