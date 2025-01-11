'''import functions

l = [100,200,300,400,500,600]
key = 500

print(functions.binary_search(l,key))'''

#regular expression module

import re

'''. - any char 
[a-z,A-Z]- char class a or b or c .... or z A or B or ...Z
[0-9]_ did=git class 0 or 1 or 2 .... or 9

+- atleast one [a-z]+
*- zero or more

^ - start of the string
$ - end of the string

? - optional
[a-z]{2,4}'''

'''s = "AAAAAABCDE1234A"
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]") #it is used to verify the pattern {9} shows the number of digits
l = re.findall(r,s)
print(l)'''

'''s = "ABCDE1234A"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$") #it only shows the vaild pattern
l = re.findall(r,s)
print(l)'''

'''s ="8123456789"
r = re.compile("^[2-9][0-9]{9}$")#[2-6] define the first char of the first digit and [2-6] define remaning digits we can give any number
l = re.findall(r,s)
print(l)
'''

'''#dd-mm-yyyy
s = "30-12-2002"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l = re.findall(r,s)
print(l)
'''





