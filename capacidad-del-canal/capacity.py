import numpy as np
import math

# Contruye una matriz de probabilidades de transición
filename = './datos.txt'
with open(filename, 'r') as f:
    matriz = [[float(num) for num in line.split(',')] for line in f]

matriz = np.array(matriz)
print(matriz)
print('')

num_rows, num_cols = matriz.shape

probabilities = []
for x in range(num_rows):
    probabilities.append(input('Introduzca la probabilidad %d: ' %x))

print(probabilities)
print('')

sumP = 0
for x in range(len(probabilities)):
    sumP = sumP + float(probabilities[x])

# print(sumP)

sumi = 0
for i in range(0, num_rows):
    pi = probabilities[i]
    sumk = 0
    for j in range(0, num_cols):
        qij = matriz[i][j]
        sumt = 0
        for t in range(0, num_rows):
            sumt += float(probabilities[t]) + matriz[t][j]
        sumk += float(qij) * math.log(qij/sumt, 2)
    sumi += float(pi) * sumk
print(sumi)
