import re
from langdetect import detect
import sys

#italian_dictionary.get_definition('causalexx',limit=1,all_data=False)
abbrevs = 0
totglosses = 0
totrefs = 0
totfastr = 0
totfas = 0
curfirstlet = ''
sawheads = {}
terms = {}
terms['acc'] = "accusativo"
terms['agg'] = "aggetivo"
terms['avv'] = "avverbio"
terms['cfr'] = "confronta"
terms['coll'] = "colletivo"
terms['collett'] = "colletivo"
terms['compar'] = "comparativo"
terms['cong'] = "congunzione"
terms['dat'] = "dativo"
terms['gen'] = "genitivo"
terms['imperat'] = "imperativo"
terms['inf'] = "infinitivo"
terms['interrog'] = "interrogativo"
terms['intrans'] = "intransitivo"
terms['lett'] = "letteralmente"
terms['metaf'] = "metaforicamente"
terms['nom'] = "nominativo"
terms['n. pr'] = "nome proprio"
terms['ovv'] = "ovviamente"
terms['p. e'] = "per esempio"
terms['part'] = "participio"
terms['passat'] = "passato"
terms['pers'] = "persona"
terms['pl'] = "plurale"
terms['pr'] = "presente"
terms['pres'] = "presente"
terms['prep'] = "preposizione"
terms['pron. pers'] = "pronome personale"
terms['pron. rel'] = "pronome relativo"
terms['prop'] = "propriamente"
terms['rad'] = "radice"
terms['sing'] = "singolare"
terms['suff'] = "suffisso"
terms['superlat'] = "superlativo"
terms['tpr'] = "tema di presente"
terms['tps'] = "tema di passato"
terms['trans'] = "transitivo"
terms['v'] = "vedi"
terms['voc'] = "vocativo"
terms['vocat'] = "vocativo"

oldlangs = {}
wikientry = {}
langcode = {}

oldlangs['antp'] = 'Old Persian'
wikientry['antp'] = 'https://en.wikipedia.org/wiki/Old_Persian'
langcode['antp'] = 'peo'

oldlangs['skr'] = 'Sanskrit'
wikientry['skr'] = 'https://en.wikipedia.org/wiki/Sanskrit'
langcode['skr'] = 'san'

oldlangs['arm'] = 'Classical Armenian'
wikientry['arm'] = 'https://en.wikipedia.org/wiki/Classical_Armenian'
langcode['arm'] = 'xcl'

oldlangs['z'] = 'Avestan'
wikientry['z'] = 'https://en.wikipedia.org/wiki/Avestan'
langcode['z'] = 'ave'

oldlangs['ar'] = 'Arabic'
wikientry['ar'] = 'https://en.wikipedia.org/wiki/Arabic'
langcode['ar'] = 'ara'

oldlangs['cald'] = 'Chaldean'
wikientry['cald'] = 'https://en.wikipedia.org/wiki/Chaldean_Neo-Aramaic'
langcode['cald'] = 'cld'

oldlangs['got'] = 'Gothic'
wikientry['got'] = 'https://en.wikipedia.org/wiki/Gothic_language'
langcode['got'] = 'got'

oldlangs['gr'] = 'Ancient Greek'
wikientry['gr'] = 'https://en.wikipedia.org/wiki/Ancient_Greek'
langcode['gr'] = 'grc'

oldlangs['ebr'] = 'Hebrew'
wikientry['ebr'] = 'https://en.wikipedia.org/wiki/Hebrew_language'
langcode['ebr'] = 'heb'

oldlangs['lat'] = 'Latin'
wikientry['lat'] = 'https://en.wikipedia.org/wiki/Latin'
langcode['lat'] = 'lat'

oldlangs['nord'] = 'Old Norse'
wikientry['nord'] = 'https://en.wikipedia.org/wiki/Old_Norse'
langcode['nord'] = 'non'

oldlangs['np'] = 'New Persian'
wikientry['np'] = 'https://en.wikipedia.org/wiki/Persian_language'
langcode['np'] = 'fas'

oldlangs['phl'] = 'Middle Persian'
wikientry['phl'] = 'https://en.wikipedia.org/wiki/Middle_Persian'
langcode['phl'] = 'pal'

oldlangs['sir'] = 'Syriac'
wikientry['sir'] = 'https://en.wikipedia.org/wiki/Syriac_language'
langcode['sir'] = 'syc'

oldlangs['ted'] = 'German'
wikientry['ted'] = 'https://en.wikipedia.org/wiki/German_language'
langcode['ted'] = 'deu'

oldlangs['ingl'] = 'English'
wikientry['ingl'] = 'https://en.wikipedia.org/wiki/English_language'
langcode['ingl'] = 'eng'


f = open('pizzi-tei.txt','r')
for l in f:
  print(l,end='')

f.close()
f = open('Pizzi-Glossary-Farnoosh.txt','r')

pizzinum = 0
lnum = 0
arabyods = 0

ends = ''
for l in f:
   l = re.sub('^[ ]+','',l)
   l = re.sub("^" + u'\u200c','',l)
   l = re.sub("^" + u'\uFEFF','',l)
   l = re.sub("^" + u'\u200f','',l)
   l = re.sub( u'\u200f' + '$','',l)
   l = re.sub('[ \n]+$','',l)
   l = re.sub(u'\u200c' + '$','',l)
   l = re.sub(u'\u200f' + '$','',l)
 # replace Arabic yod with Persian!
   if( re.search('ي',l)):
    arabyods = arabyods + 1
   l = re.sub('ي','ی',l)

   for foo in oldlangs:
     l = re.sub('\\b' + foo + '\\.[ ]+' + '([^ <,.]+)','<term n="' + foo + ':' + wikientry[foo] + '">' + oldlangs[foo] + '</term> <foreign xml:lang="' + langcode[foo] + '-tr">\g<1></foreign>',l)

   for foo in terms:
      l = re.sub('\\b' + foo + '\\.','<term n="' + foo + '">'+ terms[foo] + "</term>",l)
   m = re.search('^#([^#]+)#[ ]*([^<, ]+)',l)
   if( m ):
     curhead = re.sub('[;]','',m[2])
     curhead = re.sub("'","gh",curhead)
     curhead = re.sub("ț","th",curhead)
     if(curhead in sawheads):
       sawheads[curhead] = sawheads[curhead] + 1
     else:
       sawheads[curhead] = 1
     l = re.sub('^#([^#]+)#[ ]*([^<, ]+)[ ,]*',ends + '<div type="textpart" subtype="entry" xml:id="' + curhead + '-' + str(sawheads[curhead])+ '">\n<head xml:lang="fas">\n\g<1>\n</head>\n<head xml:lang="fas-tr">\g<2></head>\n<p>',l)
     ends = '</p></div>\n\n'
   if( re.search('\\b2\)',l)): # if we have more than one word sense
     l = re.sub('\\b1\)[ ]*','</p>\n<div type="textpart" subtype="wsense" n="1">\n<p>',l)
     l = re.sub('\\b([2-9])\)[ ]*','</p></div>\n<div type="textpart" subtype="wsense" n="\g<1>">\n<p>',l)
     ends = '</p>\n</div>\n</div>\n\n'
   l = re.sub('(eng|lat|got|deu|non|grc)\-tr','\g<1>',l)
   l = re.sub('<p></p>\n','',l)

     #print("curf",curfirstlet,l)
   l = re.sub('([——\-\–][ ]*)([a-zâêîûôćḫǧšḥč]+\.[ ]+[a-zA-Z\-âêîûôćḫǧšḥč ]+)(,)','\g<1><foreign xml:lang="fas-tr2">\g<2></foreign>\g<3>',l)
   while( re.search('(;[ ]+|;[ ]*[–]+[ ]*|</term>[ ]+)([\.a-zA-Z\-âêîûôćḫǧšḥč ]+)([), ;\.])',l)):
    m = re.search('(;[ ]+|;[ ]*[–]+[ ]*|</term>[ ]+)([\.a-zA-Z\-âêîûôćḫǧšḥč ]+)([), ;\.])',l)
   
    if(m):
     fpat = m[2]
     if( re.search('[âêîûôćḫǧšḥč]',fpat) or re.search('\b[a-z]\.',fpat)):
      l = re.sub('(;[ ]+|;[ ]*[–]+[ ]*|</term>[ ]+)([\.a-zA-Z\-âêîûôćḫǧšḥč ]+)([), ;\.])','\g<1><foreign xml:lang="fas-tr3">\g<2></foreign>\g<3>',l,1)
     else:
      l = re.sub('(;[ ]+|;[ ]*[–]+[ ]*|</term>[ ]+)([\.a-zA-Z\-âêîûôćḫǧšḥč ]+)([), ;\.])','\g<1><x>\g<2>\g<3>',l,1)
    
   l = re.sub('<x>','',l)
   l = re.sub('(forma abbreviata|senso passivo)','<term>\g<1></term>',l)
   l = re.sub('(</term>[ ]+di[ ]+|<term n="v">vedi</term>[ ]+)([a-zA-Z\-âêîûôćḫǧšḥč]+)([\),;])','\g<1><foreign xml:lang="fas-tr4">\g<2></foreign>\g<3>',l)
   l = re.sub('(<foreign xml:lang="fas-tr3">)([ \-]+ )','\g<2>\g<1>',l)
   l = re.sub('-tr[0-9]','-tr',l)

   l = re.sub('(;[ ]+)([a-zâêîûôćḫǧšḫḥč]\.[ ]+[\.a-zA-Z\-âêîûôćḫǧšḥč ]+)([), ;\.])','\g<1><foreign xml:lang="fas-tr">\g<2></foreign>\g<3>',l)
   while( re.search('<foreign xml:lang="fas-tr">([a-zćḫǧšḥč]*[a-zćḫǧšḥč]\.[^<]+)',l)):
     m = re.search('<foreign xml:lang="fas-tr">([a-zćḫǧšḥč]*[a-zćḫǧšḥč])(\.[^<]+)',l)
     if(m):
      abbrevs = abbrevs + 1
      if( not re.search('^' + m[1],curhead)):
         sys.stderr.write("fail\t" +str(abbrevs) + '\t' + curhead + '\t' + m[1] + m[2] + '\n')
     l = re.sub('(<foreign xml:lang="fas-tr">)([a-zćḫǧšḥč]*[a-zćḫǧšḥč])\.([^<]+)','\g<1><abbr n="\g<2>">' + curhead + '</abbr>\g<3>',l,1)
   l = re.sub('(ref|foreign)(>,[ ]+)([a-z]+)([),])','\g<1>\g<2><gloss>\g<3></gloss>\g<4>',l)

   l = re.sub('(</ref>)([ ]+e[ ]+)([a-zćḫǧšḥčâîû]+)([,\.;:])','\g<1>\g<2><foreign xml:lang="fas-tr">\g<3></foreign>\g<4>',l)
   workl = re.sub('<foreign[^>]+>[^<]+</foreign>',' ',l)
   workl = re.sub('<ref[^>]+>[^<]+</ref>',' ',workl)
   workl = re.sub('<gloss[^>]+>[^<]+</gloss>',' ',workl)
   workl = re.sub('<term[^>]*>[^<]+</term>',' ',workl)
   workl = re.sub('<[^>]+>',' ',workl)
   workl = re.sub('[\.,;!"\'()]+',' ',workl)
   words = workl.split()

   l = re.sub('(infinitivo|participio|presente||vocativo)(</term>)([ ]+)([^< ,\.;:]+)','\g<1>\g<2>\g<3><foreign xml:lang="fas-tr">\g<4></foreign>',l)
   
   print(l)
   
   refs = re.findall('"fas-tr',l)
   totfastr = totfastr + len(refs)
   
   refs = re.findall('"fas"',l)
   totfas = totfas + len(refs)
   
   glosses = re.findall('<gloss',l)
   totglosses = totglosses + len(glosses)
   
   refs = re.findall('<ref',l)
   totrefs = totrefs + len(refs)

f.close()
sys.stderr.write('totfas\t' + str(totfas) + '\ttotfastr\t' + str(totfastr) + '\ttotrefs\t' + str(totrefs)+'\tglosses\t'+ str(totglosses) + '\n')
print('</p>\n</div>\n</body>\n</text>\n</TEI>')

#print(arabyods)
