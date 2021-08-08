def star(m):
  for i in range(m):
    print('*', end='')
  print()
m = int(input('First demention?\n'))
n = int(input('2nd demention?\n'))

star(m)

for i in range(n-2):
  print('*', end='')
  for j in range(m-2):
    print(' ', end ='')
  print('*')

star(m)