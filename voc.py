import re
import sys
f = open("Pizzi-Glossary-Farnoosh.txt", 'r')

pvoc = {}
lemcnt = {}
xlits = {}
fulls = 0
hyphs = 0
for l  in f:
   m = re.search('#([^#]+)#[ ]*([^ ,\.;:]+)',l)
   if(m):
     perslemma = m[1]
     persxlit = m[2]
     if( perslemma in xlits ):
      if( not re.search('\\b'+persxlit+'\\b',xlits[perslemma])):
        xlits[perslemma] = xlits[perslemma] + ':' + persxlit
     else:
        xlits[perslemma] = persxlit

     lemcnt[perslemma] = 0
     fulls = fulls + 1
     pvoc[re.sub('-',u'\u200c',perslemma)] = 0
     
     if( re.search('-',perslemma)):
      pvoc[re.sub('-','',perslemma)] = 1
      lemcnt[re.sub('-','',perslemma)] = 0
      hyphs = hyphs + 1
   m = re.search('<foreign xml:lang="fas">([^<]+)',l)
   if( m ):
     if( re.search('-',m[1])):
      pvoc[re.sub('-','',m[1])] = 1
     pvoc[re.sub('-',u'\u200c',m[1])] = 1
     lemcnt[re.sub('-',u'\u200c',m[1])] = 0

f.close()


f = open('pizzi-readings.fa.xml')

curline = ''
curreading = ''
for l in f:
     m = re.search('reading" n="([0-9]+)',l)
     if(m):
       curreading = m[1]
     m = re.search('<l n="([0-9]+)"',l)
     if(m):
       curline = m[1]
     if(re.search('[a-zA-Z]',l)):
       continue
     l = re.sub('[\[\]]','',l)
     words = l.split()
     for foo in words:
         savew = re.sub(u'\u200f','-',foo)
         savew = re.sub(u'\u200c','-',savew)
         foo = re.sub("^" + u'\u200c','',foo)
         foo = re.sub("^" + u'\u200f','',foo)
         foo = re.sub(u'\u200c' + '$','',foo)
         foo = re.sub(u'\u200f' + '$','',foo)
         #foo = re.sub("\]",'',foo)
         #foo = re.sub("\[",'',foo)
         if( foo in pvoc):
              if( savew in xlits):
                 persxlit = xlits[savew]
              else:
                 persxlit = 'noxlit'
              print(curreading + '.' + curline,savew,re.sub(u'\u200c','-',foo),persxlit,sep='\t')
              if( foo in lemcnt):
               lemcnt[foo] = lemcnt[foo]  + 1
              else:
               lemcnt[foo+'hyphen'] =  1
         else:
              #print('fail',foo)
              print(curreading + '.' + curline,savew,'fail','noxlit',sep='\t')

f.close()


for foo in lemcnt:
  print(lemcnt[foo],re.sub(u'\u200c','-',foo),'lemcnt',sep='\t')


sys.stderr.write('hyphs\t'+str(hyphs) + '\tfulls\t' + str(fulls) +'\n')
