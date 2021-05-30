freq = [0.15, 0.2, 0.1, 0.22, 0.17, 0.16]
# freq = [0.15, 0.16, 0.2, 0.3, 0.19]
# freq = [0.08, 0.1, 0.05, 0.2, 0.3, 0.16, 0.11]

a = [0]
b = [freq[0]]
l = freq

for i, f in enumerate(freq):
  print(i)
  if(i == len(freq) - 1):
    break
  else:
    a.insert(i + 1, round(b[i], 4))
    b.insert(i + 1, round(a[i + 1] + l[i + 1], 4))

print("Alfa:", a)
print("Beta:", b)
print("Longitud:", l)
