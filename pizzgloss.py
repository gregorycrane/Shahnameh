import re

f = open('pizzi-tei.txt','r')
for l in f:
  print(l,end='')

f.close()
f = open('pizzi-persian-nodouble.txt','r')

pizzinum = 0
lnum = 0
arabyods = 0
indel1 = ''
indel2 = ''
for l in f:
   l = re.sub('^[ ]+','',l)
   l = re.sub("^" + u'\u200c','',l)
   l = re.sub("^" + u'\uFEFF','',l)
   l = re.sub("^" + u'\u200f','',l)
   l = re.sub( u'\u200f' + '$','',l)
   if( re.search('Pizzi',l)):
     lnum = 0
     if( pizzinum > 0 ):
       print("</div>")
     pizzinum = pizzinum + 1
     print('<div type="textpart" subtype="reading" n="' + str(pizzinum) + '">')
   l = re.sub('[ \n]+$','',l)
   if( re.search('^[ ]*[A-Z]',l)):
     print("<head>" + l  + "</head>")
     continue

   l = re.sub(u'\u200c' + '$','',l)
   l = re.sub(u'\u200f' + '$','',l)
 # replace Arabic yod with Persian!
   if( re.search('ي',l)):
    arabyods = arabyods + 1
   l = re.sub('ي','ی',l)
   if( re.search('[\[\]]',l)):
     l = re.sub('\[\s*','',l)
     l = re.sub('\s*\]','',l)
     indel1 = '<del>'
     indel2 = '</del>'
   else: 
     indel = ''
   if( re.search('[a-zA-Z]',l)):
     lnum = 0
     print(l)
     continue
   if( re.search('^$',l)):
     continue
   lnum = lnum + 1
   print('<l n="'+str(lnum)+'">',indel1,l,indel2,"</l>",sep='\n')
f.close()
print('</div>\n</body>\n</text>\n</TEI>')

#print(arabyods)
