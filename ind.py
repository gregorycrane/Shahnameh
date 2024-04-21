from spellchecker import SpellChecker
spell = SpellChecker()
from fuzzywuzzy import fuzz
import re

pns = {}

def bestfit(w):
  r = 0
  maxr = 0
  for foo in pns:
    r = fuzz.ratio(w,foo)
    if( r > maxr ):
      bestw = foo
      maxr = r
  print(w,bestw,pns[bestw])

f = open('shahnameh-warn02.xml','r')
for l in f:
  while(re.search('[A-Z][A-Za-z\-]+',l)):
   m = re.search('([A-Z][A-Za-z\-]+)',l)
   if m[1] in pns:
    pns[m[1]] = pns[m[1]] + 1
   else:
    pns[m[1]] =  1
   l = re.sub('[A-Z][A-Za-z\-]+',' ',l,1)

f = open('warn02-index.txt','r')
for l in f:
  workl = l
  workl = re.sub('<[^>]+>',' ',workl)
  workl = re.sub('\n','',workl)
  while(re.search('[A-Za-z\-]+',workl)):
   m = re.search('([A-Za-z\-]+)',workl)
   if(not m[1] in pns and not spell.known([m[1]])):
    #print(m[1],'seen')
   #else:
    #bestfit(m[1])
    print(m[1],'unseen')
   workl = re.sub('[A-Za-z\-]+',' ',workl,1)
