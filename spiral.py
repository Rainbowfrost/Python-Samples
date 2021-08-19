import numpy as np

m = int(input('First demention?\n'))
n = int(input('2nd demention?\n'))

rb = m - 1
db = n - 1
lb = 0
ub = 1

y = 0
x = 0

direc = 'r'

a = np.empty((n,m), int)

#for i in range (m):
#  for j in range (n):
#    a[i][j]=0

#print(a)

for i in range(m * n):
  a[y][x] = i + 1

  if direc == 'r':
    if x == rb:
      y = y + 1
      rb = rb - 1
      direc = 'd'
    else:
      x = x + 1
  elif direc == 'd':
    if y == db:
      x = x - 1
      db = db - 1
      direc = 'l'
    else:
      y = y + 1
  elif direc == 'l':
    if x == lb:
      y = y - 1
      lb = lb + 1
      direc = 'u'
    else:
      x = x - 1
  elif direc == 'u':
    if y == ub:
      x = x + 1
      ub = ub + 1
      direc = 'r'
    else:
      y = y - 1
      

#print(a)
for i in range(n):
  for j in range(m):
    if a[i][j]<10:
      print(' ',end='')
    if a[i][j]<100:
      print(' ',end='')
    print(a[i][j],end='  ')
  print()
