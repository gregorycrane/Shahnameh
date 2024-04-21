#https://www.babelstone.co.uk/Unicode/whatisit.html
#http://pinyin.info/unicode/diacritics.html
#ایستاد  istâd
import re

lastxchar = ''
p2x = {}

p2x['ب'] = 'b'
p2x['پ'] = 'p'
p2x['ت'] = 't'
p2x['ث'] = 'ṯ'
p2x['ج'] = 'ǧ'
p2x['چ'] = 'č'
p2x['ح'] = 'ḥ'
p2x['خ'] = 'ḫ'
p2x['د'] = 'd'
p2x['ذ'] = 'ẕ'
p2x['ر'] = 'r'
p2x['ز'] = 'z'
p2x['ژ'] = 'ž'
p2x['س'] = 's'
p2x['ش'] = 'š'
p2x['ص'] = 'ṣ'
p2x['ض'] = 'ẓ'
p2x['ط'] = 'ṭ'
p2x['ظ'] = 'ẓ'
p2x['ع'] = 'ʿ'
p2x['غ'] = 'ġ'
p2x['ف'] = 'f'
p2x['ق'] = 'q'
p2x['ک'] = 'k'
p2x['گ'] = 'g'
p2x['ل'] = 'l'
p2x['م'] = 'm'
p2x['ن'] = 'n'
p2x['ه'] = 'h'
p2x['و'] = 'û'
p2x['ی'] = 'î'
p2x['ئ'] = 'y'
p2x['آ'] = 'â'
p2x['ا'] = 'â'
curi = 0
xchars = []
f = open("Pizzi-Glossary-Farnoosh.txt")
for l in f:
  m = re.search('^#([^#]+)#[ ]*([^,\.;: ]+)',l)
  if(m):
    print('curi',curi,len(xchars),end='\t')
    pers = m[1]
    pchars = list(pers)
    xlit = re.sub('sh','š',m[2])
    xlit = re.sub('kh','ḫ',xlit)
    xlit = re.sub('dh','ẕ',xlit)
    xlit = re.sub('gh','ʿ',xlit)
    xlit = re.sub('zh','ž',xlit)
    xlit = re.sub('ć','č',xlit)
    xlit = re.sub('-','',xlit)
    xchars = list(xlit)
    pers = re.sub(u'\u200C','-',pers)
    print('#',pers,xlit,sep='\t')
    curi = 0
    for foo in pchars:
     if(foo == u'\u200C' or foo == ' ' or foo == '-'):
      continue
     if foo in p2x:
      xl2 = p2x[foo]
     else:
      xl2 = 'fail1'
     if( curi < len(xchars) ):
       if( xl2 == 'û' and xchars[curi] == 'v' ):
        #print('saw û v',xl2,xchars[curi])
        if( curi < len(xchars) - 1 and xchars[curi+1] == 'u'):
          print(foo,xchars[curi]+xchars[curi+1],xl2,xchars[curi]+xchars[curi+1],'consvu',sep='\t')
          lastxchar = xchars[curi]
          curi = curi + 2
          continue
        #else:
         #print("drop",str(curi),str(len(xchars)))
       if( curi == 0 and re.search('[îû]',xchars[curi])):
         if( foo == 'ا'):
           print(foo,'init',sep='\t')
           continue
       if( curi == 0 and xchars[curi] == 'a' and foo == 'ا'):
           print(foo,xchars[curi],xl2,xchars[curi],'initshortal',sep='\t')
           lastxchar = xchars[curi]
           curi = curi + 1
           continue
       if( xl2 == 'ô' and xchars[curi] == 'o'):
          print(foo,xl2,xl2,xchars[curi],'fixo',sep='\t')
          lastxchar = xchars[curi]
          curi = curi + 1
          continue
       if( xl2 == 'î' and xchars[curi] == 'i' and curi < len(xchars) - 1 and xchars[curi+1] == 'y'):
          print(foo,xchars[curi]+xchars[curi+1],xl2,xl2,xchars[curi]+xchars[curi+1],'consiy',sep='\t')
          lastxchar = xchars[curi]
          curi = curi + 2
          continue
       if( xl2 == 'î' and xchars[curi] == 'y'):
          print(foo,xchars[curi],xl2,xchars[curi],'consy',sep='\t')
          lastxchar = xchars[curi]
          curi = curi + 1
          continue
       if( xl2 == 'û' and xchars[curi] == 'v'  and curi < len(xchars) - 1 and xchars[curi+1] == 'u'):
          print(foo,xchars[curi],xl2,xchars[curi],'consvu',sep='\t')
          lastxchar = xchars[curi]
          curi = curi + 2
          continue
       if( xl2 == 'û' and xchars[curi] == 'v'):
          print(foo,xchars[curi],xl2,xchars[curi],'consv',sep='\t')
          lastxchar = xchars[curi]
          curi = curi + 1
          continue
       if( xl2 == 'ġ' and xchars[curi] == 'g'):
          print(foo,xl2,xl2,xchars[curi],'fixg1',sep='\t')
          curi = curi + 1
          continue
       if( xl2 == 'č' and xchars[curi] == 'c'):
          print(foo,xl2,xl2,xchars[curi],'fixc',sep='\t')
          curi = curi + 1
          continue
       if( xl2 == 'q' and xchars[curi] == 'k'):
          print(foo,xl2,xl2,xchars[curi],'fixq',sep='\t')
          curi = curi + 1
          continue
       if( xl2 == 'ǧ' and xchars[curi] == 'g'):
          print(foo,xl2,xl2,xchars[curi],'fixg2',sep='\t')
          curi = curi + 1
          continue
       if( xl2 == 'û' and xchars[curi] == 'u'):
          print(foo,xl2,xl2,xchars[curi],'fixu',sep='\t')
          curi = curi + 1
          continue
       if( xl2 == 'î' and xchars[curi] == 'i'):
          print(foo,xl2,xl2,xchars[curi],'fixi',sep='\t')
          curi = curi + 1
          continue
       if( xl2 == 'â' and xchars[curi] == 'u' and lastxchar == 'v'):
          print(foo,xchars[curi],xl2,xchars[curi],'aleph2u',sep='\t')
          curi = curi + 1
          continue
       if( xl2 == 'â' and xchars[curi] == 'a'):
          print(foo,xl2,xl2,xchars[curi],'fixa',sep='\t')
          curi = curi + 1
          continue
       if( re.search('[aiu]',xchars[curi]) and curi > 0):
        print(foo,xchars[curi],xchars[curi],'svow',sep='\t')
        lastxchar = xchars[curi]
        curi = curi + 1
        if( curi < len(xchars) ):
          if( xl2 == 'û' and xchars[curi] == 'v'  ):
           print(foo,xchars[curi],xl2,xchars[curi],'consv',sep='\t')
           lastxchar = xchars[curi]
           curi = curi + 1
           continue
          
          if( not xchars[curi] == xl2 ):
             comp = "fail2"
          else:
             comp = ''
          print(foo,xl2,xchars[curi],comp,sep='\t')
       else:
          if( not xchars[curi] == xl2 ):
             comp = "fail3"
          else:
             comp = ''
          print(foo,xl2,xchars[curi],comp,sep='\t')
       if( curi < len(xchars)):
        lastxchar = xchars[curi]
       curi = curi + 1
     else:
        print("missing xlit")
      
f.close()
