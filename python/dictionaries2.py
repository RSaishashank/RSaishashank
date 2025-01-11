person={'first name':'shashi','last name':'ragi','age':str(18),'place':'mncl'}
for value1 in person.values():
  print(value1.title())
  print(value1.upper())

  favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'shashi':'java',
'shashank':'c',
'sai': 'java',
'ra':'c++',
'sa':'c'

}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
 print(language.title())








