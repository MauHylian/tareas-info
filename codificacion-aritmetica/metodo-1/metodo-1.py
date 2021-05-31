from fractions import Fraction as frac
import math

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

def multinivel(freq, intervalo):
  keys = list(freq.keys())
  q = []

  prefix = ""
  alfa_i = 0
  alfa_l = 0

  alfa = []
  beta = []
  l = []

  for c in intervalo:
    index = keys.index(c)

    for i in range(index + 1):
      q.append(prefix + keys[i])

    alfa.clear()
    beta.clear()
    l.clear()

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

    prefix += c
  
  return {
    "a": alfa.pop(),
    "b": beta.pop(),
    "l": l.pop()
  }

def neal(r):
  double = [frac(r * 2)]
  binaryDigit = []

  for num in double:
    if(num >= 1):
        nextAppend = frac((num - 1)) * 2
        if(nextAppend in double):
            double.append(frac(nextAppend))
            binaryDigit.append(1)
            return binaryDigit
        double.append(frac(nextAppend))
        binaryDigit.append(1)
    else:
        nextAppend = frac(num) * 2
        if(nextAppend in double):
            double.append(frac(nextAppend))
            binaryDigit.append(0)
            return binaryDigit
        double.append(frac(nextAppend))
        binaryDigit.append(0)

valores = multinivel(freq, intervalo)

def find_t(l, start = 1):
  t = start
  while True:
    tv = 1 / (2 ** t)
    if tv <= l:
      break
    t += 1
  
  tl = t - 1

  i = 2 ** -t
  f = 2 ** -tl

  if l >= i and l <= f:
    return t

  return find_t(l, t + 1)

l = valores["l"]
t = find_t(l)

a = valores["a"]
b = valores["b"]

xa = math.ceil(a * 2 ** t)
xb = math.floor(b * 2 ** t)

x = xa
if x != xb and xb % 2 == 0:
  x = xb
cod = neal(frac(x / 2 ** t))

print("a:", a)
print("b:", b)
print("l:", l)
print()
print("t:", t)
print("xa:", a * 2 ** t, ", xb:", b * 2 ** t)
print("x:", x)
print("Expansión binaria:", cod)