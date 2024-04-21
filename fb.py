from spellchecker import SpellChecker

import re
import sys

prevpg = 0
curchap = 1

extravoc = {}

pns1 = {}
f = open("frpns.txt","r")
for l in f:
   l = re.sub('\n','',l)
   args = l.split()
   pns1[args[1]] = args[6]
   #sys.stderr.write('args'+' ' +args[1]+' ' +pns1[args[1]]+'\n')

pns1['Anderiman'] = 'pers'
pns1['Aschkesch'] = 'pers'
pns1['Barteh'] = 'pers'
pns1['Bijen'] = 'pers'
pns1['Djehn'] = 'pers'
pns1['Ferschidwerd'] = 'pers'
pns1['Firoud'] = 'pers'
pns1['Gulbad'] = 'pers'
pns1['Houscheng'] = 'pers'
pns1['Inde'] = 'pers'
pns1['Ispenoui'] = 'pers'
pns1['Keboudeh'] = 'pers'
pns1['Keriman'] = 'pers'
pns1['Khakan'] = 'pers'
pns1['Khorrad'] = 'pers'
pns1['Khosrou'] = 'pers'
pns1['Kuhrem'] = 'pers'
pns1['Meyem'] = 'pers'
pns1['Milad'] = 'pers'
pns1['Newder'] = 'pers'
pns1['Peschin'] = 'pers'
pns1['Pildendan'] = 'pers'
pns1['Rezm'] = 'pers'
pns1['Rithwan'] = 'pers'
pns1['Rivniz'] = 'pers'
pns1['Schideh'] = 'pers'
pns1['Tejaou'] = 'pers'
pns1['Thahmouras'] = 'pers'
pns1['Zadschem'] = 'pers'
pns1['Zendeh'] = 'pers'
pns1['Zerasp'] = 'pers'
pns1['Aderbeïdjan'] = 'place'
pns1['Amol'] = 'place'
pns1['Anbouh'] = 'place'
pns1['Ardebil'] = 'place'
pns1['Behar'] = 'place'
pns1['Beloudjistan'] = 'place'
pns1['Bokhara'] = 'place'
pns1['Djadj'] = 'place'
pns1['Djerem'] = 'place'
pns1['Farsistan'] = 'place'
pns1['Gangdiz'] = 'place'
pns1['Guirauguird'] = 'place'
pns1['Herat'] = 'place'
pns1['Indus'] = 'place'
pns1['Ispahan'] = 'place'
pns1['Isthakher'] = 'place'
pns1['Kasehroud'] = 'place'
pns1['Keïkorbad'] = 'place'
pns1['Kelat'] = 'place'
pns1['Kewerschan'] = 'place'
pns1['Khorasan'] = 'place'
pns1['Kolzoum'] = 'place'
pns1['Koum'] = 'place'
pns1['Koutch'] = 'place'
pns1['Madjin'] = 'place'
pns1['Maweralnahr'] = 'place'
pns1['Meïdan'] = 'place'
pns1['Merv'] = 'place'
pns1['Mervroud'] = 'place'
pns1['Nischapour'] = 'place'
pns1['Oxus'] = 'place'
pns1['Samarkand'] = 'place'
pns1['Segsar'] = 'place'
pns1['Seklab'] = 'place'
pns1['Seroudj'] = 'place'
pns1['Siped'] = 'place'
pns1['Termed'] = 'place'
pns1['Transoxane'] = 'place'
pns1['Berbers'] = 'rs+ethnic'
pns1['Sejestani'] = 'rs+ethnic'
pns1['Destour'] = 'rs+priest'
pns1['Dihkan'] = 'rs+landowner'
pns1['Dihkans'] = 'rs+landowner'
pns1['Mobed'] = 'rs+priest'
pns1['Mobeds'] = 'rs+priest'
pns1['Ard'] = 'rs+festival'
pns1['Nourouz'] = 'rs+festival'
pns1['Pehlewan'] = 'rs+hero'
pns1['Pehlewans'] = 'rs+hero'
pns1['Pehlewi'] = 'rs+language'
pns1['Sipehbed'] = 'rs+general'
pns1['Kaïsar'] = 'rs+ruler'
pns1['Keïanide'] = 'rs+ruler'
pns1['Keïanides'] = 'rs+ruler'
pns1['Sipehbeds'] = 'rs+general'
pns1['Destan'] = 'rs+destiny'
pns1['Sipehdar'] = 'rs+governor'
pns1['Sipehdars'] = 'rs+governor'
pns1['Créateur'] = 'rs+divinity'
pns1['Ormuzd'] = 'rs+divinity'
pns1['Ardibehischt'] = 'rs+month'
pns1['Deï'] = 'rs+month'
   
f.close()

f = open('mohl2-voc.txt','r')
for l in f:
   l = re.sub('^\s+','',l)
   words = l.split()
   if( (int(words[0]) > 1)):
    w = re.sub('<corr>([^<]+)<\/corr>','\g<1>',words[1])
    extravoc[w] = words[0]
extravoc['Jusqu'] = 1
extravoc['Lorsqu'] = 1
   
f.close()

prevvull = 0
pns = {}
f = open("pns-fr.txt","r")
for l in f:
 l = re.sub('\n','',l)
 args = l.split()
 pns[args[0]] = args[1]


f = open("shahnam-mohl-tei.txt","r")
for l in f:
  print(l,end="")
f.close

spell = SpellChecker(language='fr')  # French dictionary


altspells = {}
def couldbegood(word):

  if( word in extravoc):
    return(1)
  if( re.search('(ut)$',word) and spell.known([re.sub('(ut)$','u',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('(ât)$',word) and spell.known([re.sub('(ât)$','é',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('(aient)$',word) and spell.known([re.sub('(aient)$','ant',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('(ça)$',word) and spell.known([re.sub('(ça)$','cer',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('(irent)$',word) and spell.known([re.sub('(irent)$','ir',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('(irent|ons)$',word) and spell.known([re.sub('(irent|ons)$','ir',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('s$',word) and spell.known([re.sub('s$','',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('(urent|èrent)$',word) and spell.known([re.sub('(urent|èrent)$','ent',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('(èrent|comblerons)$',word) and spell.known([re.sub('(èrent|comblerons)$','er',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  if( re.search('a$',word) and spell.known([re.sub('a$','er',word)])):
    #sys.stderr.write('passed:'+word+'\n')
    return(1)
  return(0)

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

  l = re.sub('^[ ]*[“+#«\*\-.œæ][ ]*','',l)
  l = re.sub('^[ ]*[res][ ]+','',l)
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
  justwords = re.sub('[\-()0-9,—;:!?\.]+',' ',justwords)
  justwords = re.sub('[dlc][\’\']',' ',justwords)
  justwords = re.sub('[a-z]+[’\']',' ',justwords)
  justwords = re.sub('[A-Z][çôéêèâàïa-zA-Z]+',' ',justwords)
  wlist = justwords.split()
  badwords = spell.unknown(wlist)
  for foo in badwords:
  #  continue # not worth it -- too many false positives
    if( couldbegood(foo)):
      continue
    if( re.search('^[A-Z]',foo)):
     continue
#    sys.stderr.write(str(prevpg)+'\t'+foo+'\t'+spell.correction(foo)+'\n')
    subv = '<corr>' + foo + '</corr>'   
    l = re.sub('\\b' + foo + '\\b',subv,l)

  if( re.search('subtype="part"',l)):
    curchap = 2
  if( re.search('<p>',l) and re.search('[A-Z][A-Z]+',l)):
    l = re.sub('<p>','</div>\n\n<div type="textpart" subtype="chapter" n="' + str(curchap) + '">\n<head>',l)
    curchap = curchap + 1
    l = re.sub('</p>','</head>',l)
  workl = l
  while(re.search('[A-Z][A-ZÉÈÂÔÎÏÇ]+',workl)):
   m = re.search('([A-Z][A-ZÉÈÂÔÎÏÇ]+)',workl)
   tmp1 =  m[1]
   tmpw =  m[1]
   firstl = tmpw[0]
   tmpw = re.sub('^.','',tmpw.lower())
   tmpw = firstl + tmpw
   if( tmpw in pns):
    l = re.sub(tmp1,tmpw,l,1)
   else:
     if(spell.known([tmp1.lower()])):
      l = re.sub(tmp1,tmp1.lower(),l,1)
   workl = re.sub('[A-Z][A-ZÉÈÂÔÎÏÇ]+',' ',workl,1) 

  if( re.search('<head>',l)):
   l = re.sub('À ','à ',l)
   l = re.sub('A ','a ',l)
   l = re.sub("D['’]","d’",l)
   l = re.sub("L['’]","l’",l)
   l = re.sub("S['’]","s’",l)

  l = re.sub('œ','oe',l)

  workl = l
  workl = re.sub('<persName>[^<]+<\/persName>',' ',workl)
  workl = re.sub('<placeName>[^<]+<\/placeName>',' ',workl)

  l = re.sub('(Keï)[ ]+([A-Z][çôéêèâàïa-za-z]+)','<persName><roleName>\g<1></roleName> \g<2></persName>',l)
  workl = re.sub('(Keï)[ ]+([A-Z][çôéêèâàïa-za-z]+)',' ',workl)

  l = re.sub('(Zendeh)[ ]+(Rezm)','<persName>\g<1> \g<2></persName>',l)
  workl = re.sub('(Keï)[ ]+([A-Z][çôéêèâàïa-za-z]+)',' ',workl)

  l = re.sub('(Kadjar[ ]+Baschi)','<placeName>\g<1></placeName>',l)
  workl = re.sub('(Kadjar[ ]+Baschi)',' ',workl)

  l = re.sub('(Kafdjak[ ]+Taschi)','<placeName>\g<1></placeName>',l)
  workl = re.sub('(Kafdjak[ ]+Taschi)',' ',workl)

  while(re.search('[A-Z][çôéêèâàïa-za-z]+',workl)):
   m = re.search('([A-Z][çôéêèâàïa-za-z]+)',workl)
   w = m[1]
   if( w in pns1):
     #sys.stderr.write('passed3:'+w+':'+pns1[w]+':'+workl+'\n')
     if( pns1[w] == 'place'):
       l = re.sub('\\b' + w + '\\b','<placeName>' + w + '</placeName>',l)
       workl = re.sub('\\b' + w + '\\b',' ',workl)
       continue
     if( pns1[w] == 'pers'):
       l = re.sub('\\b' + w + '\\b','<persName>' + w + '</persName>',l)
       workl = re.sub('\\b' + w + '\\b',' ',workl)
       continue
     if( re.search('^rs\+',pns1[w])):
       m = re.search('^rs\+(.+)',pns1[w])
       usetype = m[1]
       l = re.sub('\\b' + w + '\\b','<rs type="' + usetype + '">' + w + '</rs>',l)
       workl = re.sub('\\b' + w + '\\b',' ',workl)
       continue
     workl = re.sub('\\b' + w + '\\b',' ',workl)
   else:
     if( spell.unknown([w]) and not couldbegood(w)):
        l = re.sub('\\b' + w + '\\b','<corr>' + w + '</corr>',l,1)
     workl = re.sub('[A-Z][çôéêèâàïa-za-z]+',' ',workl,1)
  print(l,end="")

  if( re.search('<q\\b',l) and not re.search('<\/q>[^<]+$',l)):
    inquote = 1
  if( re.search('<\/q>',l) and not re.search('<q>[^<]*$',l)):
    inquote  = 0
  l = re.sub('quote>','q>',l)

f.close
