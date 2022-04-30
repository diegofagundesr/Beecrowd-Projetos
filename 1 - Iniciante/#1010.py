# beecrowd | 1010

# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2

peca1 = input().split()
cod1 = int(peca1[0])
numero1 = int(peca1[1])
valor_unitario1 = float(peca1[2])
vt_pago1 = (numero1 * valor_unitario1)

peca2 = input().split()
cod2 = int(peca2[0])
numero2 = int(peca2[1])
valor_unitario2 = float(peca2[2])
vt_pago2 = (numero2 * valor_unitario2)

# calcular o valor total a ser pago no total de peças
valor_total = (vt_pago1 + vt_pago2)

# imprimir o valor total a ser pago
print("VALOR A PAGAR: R$", '{:.2f}'.format(valor_total))
