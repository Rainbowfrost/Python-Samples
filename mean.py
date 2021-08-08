a = int(input('First number?\n'))
b = int(input('Second number?\n'))
c = int(input('Third number?\n'))

if a < b:
  first = a
  second = b
else:
  first = b
  second = a
if c < first:
  thrid = second 
  second = first
  first = c
else:
  if c > second:
    thrid = c
  else:
    thrid = second
    second = c

print(first, second, thrid)

print(a + b + c / 3)

# A1 = a  A2 = b  A3 = c
# F1 = first  F2 = second  F3 = third