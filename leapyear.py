print ('Please enter the year')
year = int (input())
y = int (year/4)*4
#print (y)
if y == year:
  print ('This year is a leap year!')
else :
  print ('This year isn\'t a leap year!')
print ('How we calculate this is by taking the year divided by 4 and then multiplied by 4. If the answer is the same year, then it is a leap year. But if it is not the same year then it is not a leap year.')

print ('Would you like to do another one?')