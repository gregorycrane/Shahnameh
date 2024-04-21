import re
from spellchecker import SpellChecker
  
spell = SpellChecker(language='fr')  # French dictionary

#f = open("shahnameh.mohl02.xml","r")
f = open("outf.xml","r")
pns = {}
for l in f:
 l = re.sub('<[^>]+>',' ',l)
 l = re.sub('[a-z]+[’]',' ',l)
 while(re.search('[A-Z][a-zïéèàâôê]+',l)):
  m = re.search('([A-Z][a-zïéèàâôê]+)',l)
  if(spell.unknown([m[1]]) or re.search('Ir[ae]n',m[1])):
   if m[1] in pns:
    pns[m[1]] = pns[m[1]] + 1
   else:
    pns[m[1]] = 1
   #print(m[1])
  l = re.sub('[A-Z][a-zïéèàâôê]+',' ',l,1)

for foo in sorted(pns):
 print(foo,pns[foo],sep='\t')
