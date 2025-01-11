squares1=[]
for value3 in range(1,11):
       squares1.append(value3**2)#reduced a step
       print(squares1)
from multiprocessing import process
for value4 in range(1,21):
       print(value4)
from multiprocessing import process
digit=(0,1,2,3,4,5,6,7,8,9)
print(min(digit))
print(max(digit))
print(sum(digit))

from multiprocessing import process
squares2=[value**2 for value in range(1,16)]
print(squares2)

from multiprocessing import process 
sha = []
for value in range(3,10):
       shashank = (value**3)
       sha.append(shashank)
       print(sha)

from multiprocessing import process
sha =[value**3 for value in range(1,10)]
print(value)
          
computer = ['ram','rom','mouse','key board']#slicing list
print(computer[0:3])#Python stops one item before the second index you specify.
print(computer[2:])
print(computer[:3])
samecomputer = computer[:]
samecomputer.append('key')
computer.append('ssd')
print(computer)#coping the list
print(samecomputer)

#Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
#A tuple looks just like a list except you use parentheses instead of square brackets.

school=(100,20)
print(school[0])
print(school[1])
#school[0]=250
print(school)#because we’re trying to alter a tuple, which can’t be done to that type of object, Python tells us we can’t assign a new value to an item in a tuple

school=(100,200)
for value in school:
       print(value)
       school = (200,500)
       for value in school:
              print(value)#Python doesn’t raise any errors this time, because overwriting a variable is valid

if 'ram' in computer:
       print("d")
       car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

grade_list = ["A+","A-","B","B+","A+","A+","A-"]
for grade in grade_list:
 if grade == "A+":
    print("TPF")
 else:
    print("Not TPF")

