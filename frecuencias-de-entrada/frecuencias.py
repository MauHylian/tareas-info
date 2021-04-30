# Suponiendo que se tiene una matriz de probabilidades de transición
# este programa calcula las frecuencias de salida.

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

# Probabilidades que nos da el problema
# de que al transmitir cierto caracter
# recibamos otro.
probabilites = []
# probLen = input('Introduzca la cantidad de probabilidades a emplear. ')
probLen = num_rows
for x in range(int(probLen)):
    probabilites.append(input('Probabilidad: '))

print('')
print(probabilites)

matriz_completa = np.empty((num_rows, num_cols))

for i in range(num_rows):
    for j in range(num_cols):
        matriz_completa[i][j] = float(matriz[i][j]) * float(probabilites[i])

print('')
print('Matriz completa:')
print(matriz_completa)

column_sums = matriz_completa.sum(axis=0)
print('')
print('Frecuencias de salida: ', column_sums)
