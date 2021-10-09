s = input('Write a sentence here.\n')
def trimstart(s):
    i = 0
    s2 = ""
    while s[i] == " ":
        i = i + 1
    while i < len(s):
        s2 = s2 + s[i]
        i = i + 1
    return s2

def trimend(s):
    a = len(s) - 1
    s2 = ""
    while s[a] == " ":
        a = a - 1
    for i in range(0, a + 1):
       s2 = s2 + s[i] 
    return s2

def trimmiddle(s): 
    s2 = ""  
    sf = 0
    for v in range(0, len(s)):
        if s[v] != " ":
            s2 = s2 + s[v]
            sf = 0
        else:
            if sf == 0:
                s2 = s2 + s[v]
                sf = 1
    return s2

print(trimmiddle(trimend(trimstart(s))))