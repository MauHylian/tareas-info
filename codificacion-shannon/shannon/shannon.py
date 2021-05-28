import math
from fractions import Fraction as frac

fi = [0.25, 0.2, 0.2, 0.15, 0.1, 0.1]
FI = [0]
fFI = []
lk = []

for i in range(0, len(fi) - 1):
  FI.append(fi[i] + FI[i])

for F in FI:
  fFI.append(frac(float(F)).limit_denominator())


for f in fi:
  lk.append(math.ceil(math.log2(1 / f)))

print("fi:", fi)
print("FI:", FI)

print("FI (Fracción): [",end='')
for i, fF in enumerate(fFI):
  end = ', '
  if i == len(fFI) - 1:
    end = ''
  print(str(fF), end=end)
print(']')

print("lk:", lk)

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

eb = []

for i, f in enumerate(FI):
  l = lk[i]
  fF = fFI[i]
  b = []

  if f == 0:
    for i in range(l):
      b.append(0)
  else:
    b = neal(fF)[:l]

  eb.append(b)

print()
print("Expansiones binarias")
for b in eb:
  print(b)