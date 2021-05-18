import numpy as np
import math

# Contruye una matriz de probabilidades de transición
filename = './datos-examen.txt'
with open(filename, 'r') as f:
    q = [[float(num) for num in line.split(',')] for line in f]

q = np.array(q)
print(q)
print('')

num_rows, num_cols = q.shape

p = []
for x in range(num_rows):
    p.append(float(input('Introduzca la probabilidad %d: ' % x)))

print(p)
print('')

sumP = 0
for x in range(len(p)):
    sumP = sumP + float(p[x])

sum = 0
for i in range(0, num_rows):
    for j in range(0, num_cols):
        pi = p[i]
        qij = q[i][j]

        sumt = 0
        for t in range(0, num_rows):
            sumt += p[t] * q[t][j]

        sum += pi * qij * math.log(qij / sumt, 10)

print("Capacidad del canal (I(A, B)) =", sum)
