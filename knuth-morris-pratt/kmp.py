string = 'ACDCEFACEDBADFCEDAC'
print(len(string))

n = []
n.append(0)

offset = 1
x = 0
for char in range(0, len(string)):
    if(string[char + offset] == string[x]):
        x = x + 1
        n.insert((char + 1), x) # Insert at index (char + 1) element x
        print(n)
    else:
        n.insert((char + offset), 0)
        x = 0
    if(char == len(string) - 2):
        break

print('')
print('lps[] = ', n)