import re
from fuzzywuzzy import fuzz

placen = {}
persn = {}
rsn = {}

f = open('shahnameh.mohl02.xml','r')

pns = {}
for l in f:
  savel = l
  while(re.search('[a-z][ ]+([A-Z][çôéêèâàïa-zA-Z]+)',savel)):
    m = re.search('[a-z][ ]+([A-Z][çôéêèâàïa-zA-Z]+)',savel)
    curpn = m[1]
    if( curpn in pns):
      pns[curpn] = pns[curpn] + 1
    else:
      pns[curpn] =  1
    savel = re.sub('[a-z][ ]+([A-Z][çôéêèâàïa-zA-Z]+)',' ',savel)

f.close()


f = open('shahnameh-warn02.xml','r')
for l in f:
   while(re.search('<persName>([^<]+)',l)):
       m = re.search('<persName>([^<]+)',l)
       if( m[1] in persn):
         persn[m[1]] = persn[m[1]] + 1
       else:
         persn[m[1]] = 1
       l = re.sub('<persName>([^<]+)',' ',l)
       
   while(re.search('<rs type="([^"]+)">([^<]+)',l)):
       m = re.search('<rs type="([^"]+)">([^<]+)',l)
       curk = m[2] + '+' + m[1]
       if( curk in rsn):
         rsn[curk] = rsn[curk] + 1
       else:
         rsn[curk] = 1
       l = re.sub('<rs type="([^"]+)">([^<]+)',' ',l)
       
   while(re.search('<placeName>([^<]+)',l)):
       m = re.search('<placeName>([^<]+)',l)
       if( m[1] in placen):
         placen[m[1]] = placen[m[1]] + 1
       else:
         placen[m[1]] = 1
       l = re.sub('<placeName>([^<]+)',' ',l)
       
    
f.close()


def getbestm(w):
   best = 0
   type = ''
   workw = re.sub('ou','u',w)
   workw = re.sub('([Ss])ch','\g<1>h',workw)
   workw = re.sub('tch','ch',workw)
   workw = re.sub('eh$','a',workw)
   workw = re.sub('ï','i',workw)
   bestworkw = ''

   for foo in persn:
     r = fuzz.ratio(foo,workw)
     if( r > best):
       best = r
       bestm = foo
       type = 'pers'
       bestfreq = str(persn[foo])
       bestworkw = workw

   for foo in placen:
     r = fuzz.ratio(foo,workw)
     if( r > best):
       best = r
       bestm = foo
       type = 'place'
       bestfreq = str(placen[foo])
       bestworkw = workw

   for foo in rsn:
     args = foo.split('+')
     r = fuzz.ratio(args[0],workw)
     if( r > best):
       best = r
       bestm = foo
       type = 'rs' + '+' + args[1]
       bestfreq = str(rsn[foo])
       bestworkw = workw

   print(best,w,pns[w],bestworkw,bestm,bestfreq,type,sep='\t')
   return(bestm)

for foo in pns:
  bestm = getbestm(foo)
