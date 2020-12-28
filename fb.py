from spellchecker import SpellChecker

import re
import sys

prevpg = 0

prevvull = 0
f = open("shahnam-mohl-tei.txt","r")
for l in f:
  print(l,end="")
f.close

spell = SpellChecker(language='fr')  # French dictionary


def getsubw(word):
  if( word == ''):
    return('keeper')
  if( word[0].isupper()):
    return('keeper-up')
  word2 = re.sub('^.','',word)
  if( spell.word_probability(word2) > spell.word_probability(word)):
    return(word2)
  else:
    return('keeper')

inquote = 0
f = open("shahnameh.mohl02.txt","r")
for l in f:
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

  l = re.sub('[ ]+«',' <q>',l)
  l = re.sub('»',' </q>',l)
  l = re.sub('^[ ]+','',l)

  if( inquote and not re.search('<pb',l)):
   if( re.search('^[ ]*[“+#æ\-.œ«\*][ ]*',l) or re.search('^[ ]*[res][ ]+',l)):
    l = re.sub('^[ ]*[“+#«\*\-.œæ][ ]*','',l)
    l = re.sub('^[ ]*[res][ ]+','',l)
#    print('quote:',end='')
   else:
     l2 = re.sub('[;,\.!?]',' ',l)
     words = l2.split()
     if( len(words)):
      curw = []
      curw.append(words[0])
      curw2 = []
      curw2.append(re.sub('^.[ ]*','',words[0]))
      #if( spell.unknown(curw))
      if(spell.unknown(curw)):
       if( spell.known(curw2)):
    #    print('inquoteb:',end='')
        l = re.sub('^.','',l)
       else:
        if( re.search('^[a-z][A-Z]',l)):
          l = re.sub('^[a-z]','',l)
    #      print('inquotec:',end='')
    #    else:
    #      print('inquoted:',end='')
      else:
       if( not re.search('keeper',getsubw(words[0]))):
    #     print('inquotee:',end='')
         l = re.sub('^.','',l)
    #   else:
    #     print('inquotef:',end='')
    
  justwords = re.sub('<[^>]+>',' ',l)
  justwords = re.sub('[()0-9,;:!?\.]+',' ',justwords)
  justwords = re.sub('[a-z]+[’\']',' ',justwords)
  justwords = re.sub('[A-Z][a-zA-Z]+',' ',justwords)
  wlist = justwords.split()
  badwords = spell.unknown(wlist)
  for foo in badwords:
    continue # not worth it -- too many false positives
    if( re.search('^[A-Z]',foo)):
     continue
    sys.stderr.write(str(prevpg)+'\t'+foo+'\t'+spell.correction(foo)+'\n')
    subv = '<corr>' + foo + '</corr>'   
    #l = re.sub(foo,subv,l)
  print(l,end="")

  if( re.search('<q>',l) and not re.search('<\/q>[^<]+$',l)):
    inquote = 1
  if( re.search('<\/q>',l) and not re.search('<q>[^<]*$',l)):
    inquote  = 0

f.close
