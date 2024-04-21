from spellchecker import SpellChecker
spell = SpellChecker()
import re

persnames = {}
placenames = {}
placenames['Iran'] = 1
rs = {}
rstype = {}
f = open('shahnameh-warn02-index.xml','r')
for l in f:
  l = re.sub('\n','',l)
  workl = l
  while( re.search('<persName>[^<0-9]+',workl)):
   m = re.search('<persName>([^<0-9]+)',workl)
   workl = re.sub('<persName>[^>]+',' ',workl,1)
   if m[1] in persnames:
     persnames[m[1]] = persnames[m[1]] + 1
   else:
     persnames[m[1]] =  1
    
  while( re.search('<placeName>[^<0-9]+',workl)):
   m = re.search('<placeName>([^<0-9]+)',workl)
   workl = re.sub('<placeName>[^>]+>',' ',workl,1)
   if m[1] in placenames:
     placenames[m[1]] = placenames[m[1]] + 1
   else:
     placenames[m[1]] =  1
    
  while( re.search('<rs[^<]+',workl)):
   m = re.search('<rs type="([^"]+)">([^<]+)',workl)
   rstype[m[2]] = m[1]
   if m[2] in rs:
     rs[m[2]] = rs[m[2]] + 1
   else:
     rs[m[2]] =  1
   workl = re.sub('<rs[^>]+>',' ',workl,1)
    

f.close()


f = open('shahnameh-warn02a','r')
inbody = 0
for l in f:
  if( re.search('<body',l)):
   inbody = 1
  if( not inbody ):
   print(l,end='')
   continue 
  workl = l
  workl = re.sub('<[^>]+>',' ',workl)
  l = re.sub('[ ][ ]+',' ',l)
  while( re.search('([A-Z][a-z]+ [A-Z][a-z]+)',workl)):
   m = re.search('([A-Z][a-z]+ [A-Z][a-z]+)',workl)
   if(m):
    w = m[1]
    if( w in persnames):
      l = re.sub(w,'<persName>'+w+'</persName>',l)
      workl = re.sub(w,' ',workl)
    else:
      if( w in placenames):
       l = re.sub(w,'<placeName>'+w+'</placeName>',l)
       workl = re.sub(w,' ',workl)
      else:
       workl = re.sub('[A-Z][a-z]+',' ',workl,1)

  workl = l
  workl = re.sub('(<persName>|<placeName>)[^<]+(<\/placeName>|<\/persName>)',' ',workl)
  workl = re.sub('<[^>]+>',' ',workl)

  workl = re.sub('<[^>]+>',' ',workl)
  while( re.search('([A-Z][a-z]+)',workl)):
   m = re.search('([A-Z][a-z]+)',workl)
   if(m):
    w = m[1]
    if( w in persnames):
      l = re.sub('\\b'+w+'\\b','<persName>'+w+'</persName>',l)
    else:
      if( w in placenames):
       l = re.sub('\\b'+w+'\\b','<placeName>'+w+'</placeName>',l)
      else:
        if( w in rs):
         l = re.sub('\\b'+w+'\\b','<rs' + ' type="' + rstype[w] + '">'+w+'</rs>',l)
   workl = re.sub('([A-Z][a-z]+)',' ',workl,1)

  workl = l
  workl = re.sub('(<persName>|<placeName><rs[^>]*>)[^<]+(<\/placeName>|<\/persName>|<\/rs>)',' ',workl)
  workl = re.sub('<[^>]+>',' ',workl)
  workl = re.sub('[,.!?)(\+\*\-\’\—\'\"\]\[;:]',' ',workl)
  for foo in spell.unknown(workl.split()):
    matchv = '\\b' + foo + '\\b'
    subv = '<sic>' + foo + '</sic>'
    l = re.sub(matchv,subv,l)
    workl = re.sub(matchv,' ' ,workl)
  print(l,end='')
