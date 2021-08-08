n = int(input('First demention?\n'))
m = int(input('Second demention?\n'))
i = 0
j = 0
v = 0
while j < m:
  i=0
  j=j+1
  while i < j + 1:
    i=i+1
    v=v+1
    print(v,end=', ')
  print()