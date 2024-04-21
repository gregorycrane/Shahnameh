import re

f = open('pizzi1.txt','r')
lnum = 0
for l in f:
  if( re.search('^[ \n]*$',l)):
    continue
  lnum = lnum + 1
  print(str(lnum),l,end='')
