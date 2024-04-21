from unidecode import unidecode
from cltk.corpus.greek.beta_to_unicode import Replacer
from fuzzywuzzy import fuzz
import re

moscs = {}
vs = {}
bestmatches = {}
bestmatch = {}

def getbestmatch(targ):
  for foo in moscs:
    r = fuzz.ratio(foo,targ)
    if( not targ in bestmatches):
      bestmatches[targ] = str(r) + '\t' + moscs[foo]
      bestmatch[targ] = r
      continue
    if( r > bestmatch[targ]):
      bestmatches[targ] = str(r) + '\t' + moscs[foo]
      bestmatch[targ] = r
  print('final',targ,bestmatches[targ])

f = open('mosc1.txt','r')
for l in f:
 l = re.sub('^[ ]+','',l)
 l = re.sub('\n','',l)
 orgl = l
 l = re.sub('<[^>]+>',' ',l)
 if( re.search('^$',l)):
   continue
 moscs[l] = orgl
 #print('mosc',l,end='')


f.close()

f = open('10.txt','r')
for l in f:
 orgl = l
 l = re.sub('<[^>]+>',' ',l)
 l = re.sub('^[ ]+','',l)
 if( re.search('^\n',l)):
   continue
 l = re.sub('\n','',l)
 getbestmatch(l)
f.close()

#for foo in moscs:
#  for boo in vs:
#    r = fuzz.ratio(foo,boo)
#    print(r,moscs[foo],'v',boo,'\n')

