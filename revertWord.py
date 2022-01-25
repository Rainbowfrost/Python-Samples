s = input('Write a word here?\n')
m = ""

for i in range(len(s)-1,-1,-1):
    m = m + s[i]

print(m)
