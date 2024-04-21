#https://awesomeopensource.com/project/mirhmousavi/Regex.Persian.Language
import re

f = open('a.txt','r')

cursnum = 0
cursnum2 = 0
for l in f:
  l = re.sub('^[ ]+','',l)
  l = re.sub('[ ]+$','',l)
  l = re.sub('     [ ]+','،',l)
  l = re.sub('\n','',l)
  print(l)
  continue
  if( re.search('\tx',l)):
     continue
     foo = l.split('\t')
     cursnum = cursnum + 1
     cursnum2 = cursnum2 + 1
     print('<l n="' + str(cursnum2) + '.' + str(cursnum) + 'a">',foo[0],'</l>')
     cursnum2 = cursnum2 + 1
     print('<l n="' + str(cursnum2) + '.' + str(cursnum) + 'b">',foo[1],'</l>')
  else:
     print(l)
 
f.close()
