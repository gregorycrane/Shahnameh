from spellchecker import SpellChecker
spell = SpellChecker()
import re
import sys
newsent = 0

prevpg = 0
spellex = {}
spellex2 = {}
spellex2['Befit'] = 1


def checkspell(w):
  spellex['Human'] = 1
  spellex['Iran'] = 1
  spellex['Mars'] = 1
  spellex['Rum'] = 1
  if( w in spellex):
   return(0)
  if( w in spellex2):
   return(1)
  if( spell.known([w.lower()])):
     return(1)
  return(0)
  
prevvull = 0
f = open("shahnam-warn-tei.txt","r")
for l in f:
  print(l,end="")
f.close

f = open("shahnam-warn02.eng1.txt","r")
for l in f:
  if( re.search('^\s$$',l)):
    print(l,end='')
    continue
  m = re.search('<pb n="([0-9]+)"',l)
  if(m):
   curpg = int(m[1])
   if( not curpg == prevpg + 1):
     sys.stderr.write('jumped from ' + str(prevpg) + ' to ' + str(curpg) + '\n')
   prevpg = curpg

  m = re.search('n="V\.([0-9]+)"',l)
  if(m):
   curvull = int(m[1])
   if( not curvull == prevvull + 1):
     sys.stderr.write('vullers jumped from ' + str(prevvull) + ' to ' + str(curvull) + '\n')
   prevvull = curvull

  l = re.sub('^([““‘\'][ ]*[A-Z]+)','<lb/>\g<1>',l)
    
  l = re.sub('^([A-Z]+)','<lb/>\g<1>',l)
  m = re.search('<lb\/>([A-Z][a-z]*)',l)
  #if( m and spell.known([m[1].lower()]) and not m[1] == 'I' and not newsent ):
  if( m and checkspell(m[1]) and not m[1] == 'I' and not newsent ):
    #print(m[1].lower,end=':')
    sub = m[1].lower()
    l = re.sub('<lb/>([A-Z][a-z]*)','<lb/>'+sub,l)

  if( not re.search('^<mile',l) and not re.search('^[ \n]*$',l)):
   newsent = 0
  if( re.search('[?\.!][ ]*$',l) or re.search('(<\/q>|<p>|”)[\n ]*$',l)):
     newsent = 1

  l = re.sub('‘‘','“',l)

  l = re.sub('([> ])“','\g<1><q>',l)
  l = re.sub('([\.,:?!’])[ ]*”','\g<1></q>',l)
  l = re.sub('”[ ]+','</q> ',l)

  l = re.sub('s’[ ]+',"s' ",l)
  l = re.sub('([> ])[’‘]','\g<1><q>',l)
  l = re.sub('([\.,:?!])[ ]*[’‘]','\g<1></q>',l)
  l = re.sub('[’‘][ ]+','</q> ',l)
  l = re.sub('quote>','q>',l)

  l = re.sub('(<note n=")([0-9]+)','<note xml:id="n.'+str(prevpg)+'.\g<2>',l)
  l = re.sub('@([0-9]+)','<ref target="n.'+str(prevpg)+'.\g<1>'+'"/>',l)
  print(l,end="")

f.close
