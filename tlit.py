#https://www.babelstone.co.uk/Unicode/whatisit.html
#http://pinyin.info/unicode/diacritics.html
#ایستاد  istâd
import re

newxlit = ''
lastxl2 = ''
savepers = ''
pers = ''
origxlit = ''
xlit = ''
keeppersian = {}
keeppersian['â'] = 'aá'
keeppersian['č'] = 'c'
keeppersian['ġ'] = 'g'
keeppersian['ǧ'] = 'g'
keeppersian['ḫ'] = 'h'
keeppersian['î'] = 'i'
keeppersian['ô'] = 'o'
keeppersian['q'] = 'k'
keeppersian['ṯ'] = 't'
keeppersian['û'] = 'u'

keepitalian = {}
keepitalian['y'] = 'î'
keepitalian['v'] = 'û'
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
p2x[u'\u0651'] = 'shadda'
curi = 0
xchars = []
f = open("Pizzi-Glossary-Farnoosh.txt")
for l in f:
  m = re.search('^#([^#]+)#[ ]*([^,\.;: ]+)',l)
  if(m):
    if( re.sub('sh','š',origxlit) == newxlit ):
     lab = '#same'
    else:
     lab = '#diff'
    print(lab,savepers,newxlit,origxlit,sep="\t")
    newxlit = ''
    if( not curi == len(xchars)):
     print('checklem',curi,len(xchars),sep='\t')
    pers = m[1]
    savepers = re.sub(u'\u200c','-',pers )
    pchars = list(pers)
    origxlit = m[2]
    xlit = re.sub('[àá]','â',m[2])
    xlit = re.sub('sh','š',xlit)
    xlit = re.sub('ħ','ḥ',xlit)
    xlit = re.sub('kh','ḫ',xlit)
    xlit = re.sub('dh','ẕ',xlit)
    xlit = re.sub('gh','ġ',xlit)
    xlit = re.sub('zh','ž',xlit)
    xlit = re.sub('th','t',xlit)
    xlit = re.sub('ć','č',xlit)
    xlit = re.sub('ķ','q',xlit)
    xlit = re.sub('ű','û',xlit)
    #xlit = re.sub('-','',xlit)
    xchars = list(xlit)
    pers = re.sub(u'\u200C','-',pers)
    print('#',pers,xlit,sep='\t')
    curi = 0
    for foo in pchars:
     if(foo == u'\u200C' or foo == ' ' or foo == '-'):
      continue
     if foo in p2x:
      xl2 = p2x[foo]
      if(p2x[foo] == 'shadda'):
       print("repeat",lastxl2)
       xl2 = lastxl2
     else:
      xl2 = 'fail1'
     lastxl2 = xl2
     if( curi < len(xchars) ):
       if( xchars[curi] == '-'):
        newxlit = newxlit + xchars[curi]
        curi = curi + 1
        if( not curi < len(xchars)):
         continue
# match 
# û in the Persian
# to
# uv in the xliteration
       if( xl2 == 'û' and xchars[curi] == 'u' and curi < len(xchars) - 1 and xchars[curi+1] == 'v'):
          print(foo,xchars[curi]+xchars[curi+1],xl2,xchars[curi]+xchars[curi+1],'consuv',sep='\t')
          newxlit = newxlit + xchars[curi] + xchars[curi+1]
          lastxchar = xchars[curi]
          curi = curi + 2
          continue
         
       if( curi == 0 and re.search('[îû]',xchars[curi])):
         if( foo == 'ا'):
           print(foo,'init',sep='\t')
           continue
       if( curi == 0 and re.search(xchars[curi],'iau') and foo == 'ا'):
           print(foo,xchars[curi],xl2,xchars[curi],'initshortal',sep='\t')
           lastxchar = xchars[curi]
           newxlit = newxlit + xchars[curi]
           curi = curi + 1
           continue
       if( xl2 == 'î' and xchars[curi] == 'i' and curi < len(xchars) - 1 and xchars[curi+1] == 'y'):
          print(foo,xchars[curi]+xchars[curi+1],xl2,xl2,xchars[curi]+xchars[curi+1],'consiy',sep='\t')
          lastxchar = xchars[curi]
          newxlit = newxlit + xchars[curi] + xchars[curi+1]
          curi = curi + 2
          continue
       if( xl2 == 'û' and xchars[curi] == 'v'  and curi < len(xchars) - 1 and xchars[curi+1] == 'u'):
          print(foo,xchars[curi],xl2,xchars[curi],'consvu',sep='\t')
          lastxchar = xchars[curi]
          newxlit = newxlit + xchars[curi]
          curi = curi + 2
          continue
       if( xl2 == 'â' and xchars[curi] == 'u' and lastxchar == 'v'):
          newxlit = newxlit + xchars[curi]
          print(foo,xchars[curi],xl2,xchars[curi],'aleph2u',sep='\t')
          curi = curi + 1
          continue
       if( xchars[curi] in keepitalian and keepitalian[xchars[curi]] == xl2):
          print(foo,xchars[curi],xl2,xchars[curi],'keepitalian',sep='\t')
          newxlit = newxlit + xchars[curi]
          curi = curi + 1
          continue

       if( xl2 in keeppersian and re.search(xchars[curi],keeppersian[xl2])):
          print(foo,xl2,xl2,xchars[curi],'keeppersian',sep='\t')
          newxlit = newxlit + xl2
          curi = curi + 1
          continue

       if( re.search('[aiu]',xchars[curi]) and curi > 0):
        print(foo,xchars[curi],xchars[curi],'svow',sep='\t')
        newxlit = newxlit + xchars[curi]
        lastxchar = xchars[curi]
        curi = curi + 1
        if( curi < len(xchars) and xchars[curi] == '-'):
         newxlit = newxlit + xchars[curi]
         curi = curi + 1
        if( curi < len(xchars) ):
          if( (xl2 == 'û' and xchars[curi] == 'v') or (xl2 == 'î' and xchars[curi] == 'y')  ):
           print(foo,xchars[curi],xl2,xchars[curi],'cons' + xchars[curi],sep='\t')
           newxlit = newxlit + xchars[curi]
           lastxchar = xchars[curi]
           curi = curi + 1
           continue
          
          if( not xchars[curi] == xl2 ):
             comp = "fail2"
          else:
             comp = ''
          newxlit = newxlit + xl2
          print(foo,xl2,xchars[curi],comp,sep='\t')
          curi = curi + 1
          continue
       else:
          if( not xchars[curi] == xl2 ):
             comp = "fail3"
          else:
             comp = ''
          newxlit = newxlit + xl2
          print(foo,xl2,xchars[curi],comp,sep='\t')
       if( curi < len(xchars)):
        lastxchar = xchars[curi]
       curi = curi + 1
     else:
        print("missing xlit")
      
f.close()
