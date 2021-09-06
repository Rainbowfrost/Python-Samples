s = input('Write a sentence here?\n')

def func1(Cha):
  if Cha >= 'A' and Cha <= 'z':
    return True
  else:
    return False

for i in range(len(s)): 
  print(s[i],end=' ')
  if func1(s[i]):
    print('Letter',end=' ')
    if not func1(s[i-1]) or i == 0:
      print(', begining of the word',end=' ')
  else:
    print('Not a Letter',end=' ')
  print()

#print(len(s)-1)
