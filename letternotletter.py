s = input('Write a sentence here?\n')

def func1(Cha):
  if Cha >= 'A' and Cha <= 'z':
    return True
  else:
    return False

for i in range(len(s)): 
  print(s[i],end=' ')
  if func1(s[i]):
    print('Letter')
  else:
    print('Not a Letter')
print()

#print(len(s)-1)