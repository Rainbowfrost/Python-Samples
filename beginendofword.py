s = input('Write a sentence here?\n')

def func1(Cha):
  if Cha >= 'A' and Cha <= 'z':
    return True
  else:
    return False

lenght_of_the_string = len(s)

for i in range(len(s)): 
  print(s[i],end=' ')
  if func1(s[i]):
    print('Letter',end=' ')
    if i == 0 or not func1(s[i-1]):
      print(', begining of the word',end=' ')
    if i ==(len(s)-1) or not func1(s[i+1]):
      print(', end of the word',end=' ')
  else:
    print('Not a Letter',end=' ')
  print()

#print(len(s)-1)
