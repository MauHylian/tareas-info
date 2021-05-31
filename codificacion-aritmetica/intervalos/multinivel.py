freq = {
  "a": 0.15,
  "b": 0.2,
  "c": 0.1,
  "d": 0.22,
  "e": 0.17,
  "f": 0.16
}

keys = list(freq.keys())
print(keys)

intervalo = input("Intervalo: ")
redondear = input("Redondear (s, n): ") == "s"

q = []

prefix = ""
alfa_i = 0
alfa_l = 0

def print_float_arr(name, arr):
  print(name, end=' ')
  print("[", end='')
  for i, v in enumerate(arr):
    if redondear:
      print(round(v, 6), end='')
    else:
      print(v, end='')
    if i != len(arr) - 1:
      print(", ", end='')
  print("]")

for c in intervalo:
  index = keys.index(c)

  for i in range(index + 1):
    q.append(prefix + keys[i])

  alfa = []
  beta = []
  l = []

  print(q)

  beta_i = alfa_i

  while len(q) > 0:
    intervalo = q.pop(0)
    
    alfa_l = beta_i
    alfa.append(alfa_l) # alfa

    l_mult = 1
    for c in intervalo:
      l_mult *= freq[c] # l
    
    l.append(l_mult)

    beta_i += l_mult # beta
    beta.append(beta_i)

  alfa_i = alfa_l

  print_float_arr("a", alfa)
  print_float_arr("b", beta)
  print_float_arr("l", l)
  print()

  prefix += c