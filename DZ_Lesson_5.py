import os

f = open('input.txt', 'r')
f2 = open('output.txt', 'w')
for i in f:
    i = i.replace('\n', '')
    s = i.split(' ')
    if s[1] == '+':
        a = int(s[0]) + int(s[2])
        f2.writelines(str(a))
    if s[1] == '-':
        b = int(s[0]) - int(s[2])
        f2.write('\n')
        f2.writelines(str(b))
    if s[1] == '*':
        c = int(s[0]) * int(s[2])
        f2.write('\n')
        f2.writelines(str(c))
    if s[1] == '/':
        d = int(s[0]) / int(s[2])
        f2.write('\n')
        f2.writelines(str(d))
