

s = input('Write amount here?')
x = s.split()
tp = 0
p = 0
for y in x:
    tp = tp + p
    if y == '1':
        p = 1
    elif y == '2':
        p = 2
    elif y == '3':
        p = 4
    elif y == '4':
        p = 7
    elif y == '6':
        p = 15
    elif y == '8':
        p = 21
    else:
        print("Come on! It is not that hard! You can only use 1 2 3 4 6 8!")
        quit()
    tp = tp + p
    
    

print("The end result is...")
print(tp)
