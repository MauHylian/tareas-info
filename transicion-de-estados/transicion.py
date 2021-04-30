# Suponiendo que se tiene una matriz de transición
# este programa calcula la información mutua y la
# entropía en un problema de transición de estados

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

# Extrae las probabilidades diferentes que hay
# en la matriz así como sus frecuencias en la misma
uniqueProbabilities, occurCount = np.unique(matriz, return_counts=True)

uniqueProbabilities = list(uniqueProbabilities)
occurCount = list(occurCount)

print("Unique Probabilities : ", uniqueProbabilities)
print("Occurrence Count : ", occurCount)
print('')

# Elimina la primer probabilidad, ya que en este programa
# las probabilidades de transición nulas son transformadas
# en ceros, y las listas van de menor a mayor.
del uniqueProbabilities[0], occurCount[0]

print("Updated Unique Probabilities : ", uniqueProbabilities)
print("Updated Occurrence Count : ", occurCount)
print('')

# Crea un diccionario que relaciona
# probabilidad con frecuencia
zipper = zip(uniqueProbabilities, occurCount)
dictionary = dict(zipper)

print(dictionary)

# Calcula información mutua con la fórmula:
# -ocurrencia * LN(probabilidad)
info = []
for probs, occurs in zip(uniqueProbabilities, occurCount):
    info.append(round(((-1 * float(occurs)) * math.log(float(probs))), 2))

print(info)

ent = []
for infs, probs in zip(info, uniqueProbabilities):
    ent.append(round(float(infs) * float(probs) , 2))

print(ent)