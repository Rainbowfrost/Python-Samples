s = input('Write a word here.\n')

def isPalindrone(s):
    i = 0
    k = len(s) - 1
    while i <= k:
        if s[i] != s[k]:
            return False
        i = i + 1
        k = k - 1
    return True

if isPalindrone(s):
    print("This is a Palindrone.",end='')
else:
    print("This is not a Palindrone.",end='')


