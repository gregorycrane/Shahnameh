import re

f = open('shahnam-warn-tei.txt','r')
for l in f:
  print(l,end='')
f.close()

adddiv = 1

f = open('warn02-index.txt','r')
for l in f:
  if( re.search('(treatise)',l)):
   l = re.sub('(<head>)([A-Z][^<]+)','\g<1><title>\g<2></title>',l)
  if( re.search('(Dragon|mythological)',l)):
   l = re.sub('(<head>)([A-Z][^<]+)','\g<1><rs type="mythologicalcreature">\g<2></rs>',l)
  if( re.search('(tribe|race|people)',l)):
   l = re.sub('(<head>)([A-Z][^<]+)','\g<1><rs type="ethnic">\g<2></rs>',l)
  if( re.search('(Canopus|planet|star|constellation)',l)):
   l = re.sub('(<head>)([A-Z][^<]+)','\g<1><rs type="heavenlybody">\g<2></rs>',l)
  if( re.search('(horse)',l)):
   l = re.sub('(<head>)([A-Z][^<]+)','\g<1><rs type="horse">\g<2></rs>',l)
  if( re.search('(Indra|Neryosang|demon|angel|Daevas|Devil|div[, ]|Agni|Evil Principle|Good Principle|spirit|Ahura Mazda)',l)):
   l = re.sub('(<head>)([A-Z][^<]+)','\g<1><rs type="divinity">\g<2></rs>',l)
  if( re.search('(sea|lake|fire-temple|pass of|district|cape|forest|garden|province|stronghold|battle of|desert|fortress|region|city|river|country|place|mountain)',l)):
   l = re.sub('(<head>)([A-Z][^<]+)','\g<1><placeName>\g<2></placeName>',l)
  if( re.search('(chieftain|dynastic title|wife|Professor|keeper|moralist|ruler|hero|brother|sister|[fF]ather|uncle|scribe|Shah|Sultan|Khalif|son |daughter|mother|king)',l)):
   l = re.sub('(<head>)([A-Z][^<]+)','\g<1><persName>\g<2></persName>',l)
 
  l = re.sub('<pe>','<persName>',l)
  l = re.sub('<\/pe>','</persName>',l)
  l = re.sub('<pl>','<placeName>',l)
  l = re.sub('<\/pl>','</placeName>',l)
  if( re.search('type="letter"',l)):
    adddiv = 0
  if( re.search('^<head',l)):
   if( adddiv):
     print('\n</div>\n\n',end='')
   l = re.sub('^<head>','<div type="textpart"><head>',l)
   adddiv = 1
  else:
    l = re.sub('(.+)','<p>\g<1></p>',l)
  l = re.sub(' ([0-9]+)([<, \.\n]+)',' <ref target="p\g<1>">\g<1></ref>\g<2>',l)
  l = re.sub(' ([0-9]+)([<, \.\n]+)',' <ref target="p\g<1>">\g<1></ref>\g<2>',l)
  l = re.sub('(<\/head>)[, ]*(.+)','\g<1> <p>\g<2></p>',l)
  l = re.sub('<p>(<\/div>)<\/p>','\g<1>',l)
  l = re.sub('<p>(<div.+)</p>$','\g<1>',l)
  l = re.sub('head1','head',l)
  print(l,end='')

print("\n</div>\n</div>\n</body>\n</text>\n</TEI>\n")
