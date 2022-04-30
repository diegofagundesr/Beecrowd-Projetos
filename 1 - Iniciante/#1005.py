# beecrowd | 1005

# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5
# Obs : Cada nota pode ir de 0 até 10.0, sempre com uma casa decimal

# ler dois de ponto flutuante, A e B
A = float(input())
B = float(input())

# calcular a média das notas, levando em conta o peso das notas
media = ((A*3.5)+(B*7.5)) / 11

# Imprimir a media das notas atribuída à mensagem "MEDIA"
print("MEDIA ="'{: .5f}'.format(media))
