# Suponiendo que se tiene una lista de probabilidades
# este programa calcula la información mutua y la
# entropía en un problema de transmisión de datos

import math

filename = './datos.txt'

# Recibe un archivo con las probabilidades
with open(filename) as f:
    prob = f.readlines()
prob = [x.strip() for x in prob]

print(prob)

# Calcula información mutua
info = []
for num in prob:
    info.append(-1*(round(math.log(float(num), 2), 2)))

print(info)

# Calcula entropía
ent = []
for probs, infs in zip(prob, info):
    ent.append(round((float(probs) * float(infs)), 2))

print(ent)