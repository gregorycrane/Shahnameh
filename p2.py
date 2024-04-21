import re

f = open('a.txt','r')

cursnum = 0
cursnum2 = 0
for l in f:
  l = re.sub('^[ ]+','',l)
  l = re.sub('[ ]+$','',l)
  l = re.sub('     [ ]+','\t',l)
  l = re.sub('\n','',l)
  words = l.split()
  for foo in words:
    print(foo)
  continue
  print(l)
