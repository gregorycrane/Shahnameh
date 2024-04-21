from spellchecker import SpellChecker

spell = SpellChecker(language='fr')  # French dictionary
print(spell['élégante'])

foo = 'rque le roi prenne une autre'
fool = foo.split()
misspelled = spell.unknown(fool)
print(misspelled)
for word in misspelled:
  print(spell.correction(word))
