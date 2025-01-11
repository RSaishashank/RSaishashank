'''print("number \t \t square")

print("1 \t\t "+str(1*1))
print("2 \t\t "+str(2*2))
print("3 \t\t "+str(3*3))
print("4 \t\t "+str(4*4))
print("5 \t\t "+str(5*5))'''

'''def number():
    for values in range(1,6):
     for value in zip(values):
        print(value)

def square():
    for values in range(1,6):
     for value in zip(values):
        value=value**2
        print(value)

def cube():
    for values in range(1,6):
     for value in zip(1,6):
        value = value**3
        print(value)
    
print("Number \t\t Square \t\t cube")
print(number() ,square() ,cube())  '''

'''print("number \t\t square \t\t cube")
print("1 \t\t"+str(1*1),"\t\t"+str(1*1*1))
print("2 \t\t"+str(2*2),"\t\t"+str(2*2*2))
print("3 \t\t"+str(3*3),"\t\t"+str(3*3*3))
print("4 \t\t"+str(4*4),"\t\t"+str(4*4*4))
print("5 \t\t"+str(5*5),"\t\t"+str(5*5*5))
print("6 \t\t"+str(6*6),"\t\t"+str(6*6*6))'''

'''length = float(input("area of A : "))
width = float(input("area of B : "))
formula = length*width
print(formula)'''

'''name = input("your address")
name1 = input("your marks")
print("Your address is"+name+" And your marks is"+name1)'''


'''marks = int(input())
#print(type(marks))
if marks >=60:
    print("your are eligible to join the college")
else :
    print("sorry! you cannot take admission, you need "+str(60-marks)+" marks more to take admission5")'''

'''a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the thrid number"))
print("addition"+str(a+b+c))
print("subtraction"+str(a-b-c))
print("multiply"+str(a*b*c))
print("division"+str(a/b/c))
print("mod of three number"+str(a%b%c))'''

'''A = {5,12,52,0,8}
B = {2,5,1,9,8}
C = {4,5,6,0,10}
d = A.union(B,C)
print(d)'''

'''A = {5,12,52,0,8}
B = {2,5,1,9,8}
C = {4,5,6,0,10}
d = A.intersection(B,C)
print(d)'''
'''
A = {12,2,0,3,8}
B = {15,10,12,3,6}
d = A.difference(B)
print(d)
'''

'''a = int(input("enter the number"))
for i in range(1,11):
    print(str(2)+"*"+str(a)+"="+str(i*a))'''


'''def table(num):
    for i in range(1,11):
        print(str(2)+"*"+str(num)+"="+str(i*num))

table(5)'''

'''a = int(input("Enter the 1st subject marks : "))
b = int(input("Enter the 2st subject marks : "))
c = int(input("Enter the 3st subject marks : "))
d = int(input("Enter the 4st subject marks : "))
e = int(input("Enter the 5st subject marks : "))
f = int(input("Enter the 6st subject marks : "))

marks = int(input("enter 1 to get total, 2 for average and 3 for percentage"))
m = a+b+c+d+e+f
k = m/600
l = m/600 *100
if marks==1:
    print("Total : "+str(m))
elif marks == 2:
    print("average : "+str(k))
else:
    print("average : "+str(l)+"%")'''


'''for i in range(5):
    for j in range(i+1):    
      print("",end=" ")
    print("")'''


'''num =5
for i in range(0,num):
    for j in range(0,num):
         if j>=5-i:
              print("*",end=" ")
         else:
              print(" ",end=" ")
         
    print("")
    '''

'''pwd = input("Enter your password")

if(pwd.isalnum()):
    print("your password is okay"+pwd)
else:
    print("sorry, we did not allow white space and special char in your password that is"+pwd)'''

'''pwd = input("Enter the password :")

if(pwd.isalnum()) and len(pwd)<=8:
    print("your password okay "+pwd)
else:
    print("your password did not meet our coditions "+pwd)
'''


'''tuple_5 = []
for i in range(6):
    tuple_5.append(int(input("Enter the value : ")))
    shashank=tuple_5
    print(tuple(shashank))
    
    
s = 0
for i in shashank:
    s+=i
print(s)
'''


'''s = []

for i in range(6):
    s.append(int(input("Enter the value : ")))
print("This is the list ")
print(s)
print("we removed the list")
s.clear()'''

'''n = int(input("Enter the number : "))

n1=n+5
print(n1)
n2=n-5
print(n2)
n3=n*5
print(n3)
n4=n/5
print(n4)
print(n1+n2+n3+n4)
'''

'''print("A")
print("B\tC")
print("D\tE\tF")
print("G\tH\tI\tJ")
print("K\tL\tM\tN")
print("O\tP\tQ\tR\tS")
print("T\tU\tV\tW\tX\tY")'''

'''d = {"name":"shashank","address":"hyderabad","contact":8328079400}
print("first user")
print(d)
d.update({"contact":8328079404})
print("updated dictory")
print(d)'''

'''a = int(input("Enter the number for a"))
b = int(input("enter the number for b"))
c = int(input("Enter the number for c"))
d = int(input("enter the number for d"))

result= d+a+2*a*b/d*(4*c+10)
print(result)'''

'''import array as arr
a = arr.array('i',[])
s=0
for i in range(5):
    a.append(int(input("Enter the number ")))
for j in range(5):
    print(a[j])
    s+=a[j]
print("sum of the number is = "+str(s))   ''' 

'''import array as arr

s = 0
a=arr.array("i",[])
for i in range(5):
    a.append(int(input("enter the number : ")))
for j in range(5):
    print(a[j])
    s = a[j]
print(max(str(s)))'''


'''import array as arr

a=arr.array("i",[])
for i in range(5):
    a.append(int(input("enter the number : ")))
print(min(a))'''

'''new = input("Enter here: ")
if (new =='a') or (new == 'e') or (new == 'i') or (new == 'o') or (new == 'u') :
    print("it is vowel")
elif new.isnumeric():
    print("it is number")
else:
    print("it is consonant")'''


'''user = input("enter the day")

if user == "sunday" or user == 'sun' or user== 'Sunday' or user == "Sun" or user == "Friday" or user == "fri" or user == "Fri":
    print("Holiday")
else:
    print("it is a working day")'''

'''def numadd(a,b):
    d=a+b
    return d

def numsub(a,b):
    d =a-b
    return d

def nummul(a,b):
    d =a*b
    return d

def numdivision(a,b):
    d =a/b
    return d
    


a = int(input("enter the 1st number"))
b = int(input("Enter the 2nd number "))
op = input("Insert a operator to perform opertation")

if op == "+":
    print(numadd(a,b))
elif op == "-":
    print(numsub(a,b))
elif op == "*":
    print(nummul(a,b))
elif op == "/":
    print(numdivision(a,b))
else:
    print("you enter invaild operator ")   ''' 

'''name = input("Enter the student name")

if name=="xyz" or name == "Xyz" or name=="XYZ":
    print("You are not allow to take admission")
else:
    print("you are allowed to take admission ")
'''

'''num = int(input("Entger the number : "))

if num%2==0:
    print("number is even")
else:
    print("number is odd")

d = num*num
print(d)'''

'''year = int(input("Enter a year"))

if (year%4==0):
    print("it is a leap year")
else:
    print("it is not a leap year")'''


'''num = int(input("enter th number "))
n = num**3
print(n)'''

'''num =int(input("enter the number"))
if num>0:
    print("it is a positive number")
elif num==0:
    print("it is zero")
else:
    print("it is a negative number")'''

'''num = int(input("enter the number"))

if num%5==0 and num%6==0:
    print("number is divisible by 5 and 6")
else:
    print("number is not divisible by 5 and 6")'''

'''num = int(input("enter the scale"))

if num ==9:
    print("10,000")
elif num ==12:
    print("20,000")
elif num ==15:
    print("40,000")
elif num ==18:
    print("50,000")
elif num ==20:
    print("70,000")
else:
    print("number is not matching the scale")'''

'''a = int(input("enter the number"))
b = int(input("enter the second number"))

def minimum(a,b):
    print("the mininum of the two numbers is "+min(str(a),str(b)))



minimum(a,b)'''


'''l = ['red','green','blue']
n = input("enter the element")
l.insert(1,n)
print(l)'''

'''color = []
for i in range(5):
    color.append(input("enter the color "))

print(color)
color.pop(1)
print(color)'''


'''student=[]
for i in range(5):
    student.append(input("enter the student name "))
    print(student)

student.pop(0) and student.pop(3)
student.sort(reverse=True)
print(student)'''

'''name = input("enter the name ")

print(name.upper())'''


'''number = []

for i in range(5):
    number.append(int(input("Enter a number ")))
    print(number)

do = tuple(number)
print(do)

def add(list_num):
    s= 0
    m=1
    for i in list_num:
        s=s+i
        m=m*i
    print("addition ="+str(s))
    print("multiplication = "+str(m))

add(do)'''

'''name = input("enter the user name : ")

def username(user):
    if (user.isalnum()) and len(user)>8:
        print("your password is "+str(user))
    else:
        print("you have entered incorrect password")



username(name)'''

'''import math 
angle=float(input("enter a angle "))
sin1=math.sin(angle)
cos1=math.cos(angle)
str2=math.sin(math.radians(angle))
cos2=math.cos(math.radians(angle))
print("sin value in degree "+str(sin1),"cos value in degree "+str(cos1))
print("sin value in radian "+str(str2),"cos value in radian "+str(cos2))
'''

'''print("number\t\t square\t\t cube\t\t Addition")
for i in range(10,0,-4):
    print(str(i)+"\t\t"+str(i*i)+"\t\t"+str(i*i*i)+"\t\t"+str(i*i)+str(i*i*i))
'''

'''s=int(input("Enter a starting no "))
e = int(input("enter a ending no "))
for i in range(s,e+1,4):
    print(i)
'''


'''s = int(input("enter a starting no, that is larger "))
e = int(input("enter a ending no that is lower "))
for i in range(s,e-1,-1):
    print(str(i))'''

    
'''for i in range(1,31):
    if i%2==0:
        print(i)'''

'''import array as arr

user = input("enter your name ")
a=arr.array('i',[])
for i in range(5):
    a.append(int(input("enter subject marks")))
total = 0
for i in range(5):
    total+=a[i]

average = total/5

print("Hi, "+user+"!")
print("Your marks is , "+str(total))
print("average marks "+str(average))
print("See your all subject marks")
print("english = "+str(a[0]))
print("AI = "+str(a[1]))
print("Physics = "+str(a[2]))
print("Computer = "+str(a[3]))
print("Math = "+str(a[4]))
'''

'''a = int(input("enter the number :"))
b = int(input("enter the second number :"))

a = a+b#10+2 = 12 store in a
b=a-b#12-2=10 store in b
a=a-b#12-10=2 store in a
print(a)
print(b)'''

'''s = float(input("enter seconds to convert to hour : "))
h =s/3600
print("you entered "+str(s)+"s")
print(str(h)+"seconds is converted to hour that is "+str(s)+"h")'''

'''b = float(input("Enter Base "))
h = float(input("Enter height "))
B=b*b
H=h*h
area_traingle=(B*H)/2
print("Area of the triangle is = "+str(area_traingle))'''


'''import datetime

date1 = input("enter the 1st date \n in this formate m/d/full year")
date2 = input("enter the 2nd date \n in this formate m/d/full year")

date_format = "%m/%d/%y"
d1 = datetime.strptime(date1,date_format)
d2 = datetime.strptime(date2, date_format)
diff = d2-d1
print("Difference between two days is = "+str(diff.days))
'''

'''sen = input("enter the sentence ")
reverse= ""
for i in sen:
    reverse=i+reverse
print(f' "{reverse}"'+".")'''

'''
1 day = 24h
one year = 365*24 = 8760h
1h = 3600s
8760h into s?
8760*3600 = 31536000s
'''

'''age = float(input("Enter your age "))
age_int=age*31536000
age_min=age*3600
age_hour=age*24
print("Your age is "+str(age))
print("Your age in secinds is "+str(age_int))
print("Your age in minutes is "+str(age_min))
print("Your age in hours is "+str(age_hour))'''

'''import math
no = int(input("Enter a number to find its factorial "))
fac_of=math.factorial(no)
print("Your number is "+str(no))
print("Factorial of "+str(no)+"is"+str(fac_of))'''


'''n=int(input("enter the number"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    print(factorial)'''
    
'''from datetime import datetime
val = input("do you want to get date and date yes or no")

def display(v):
    if (v=="yes"):
        print(datetime.now())
    else:
        pass

display(val)'''

'''valu = int(input("enter the number "))

def decimaltobin(num):
    if num>=1:
        decimaltobin(num//2)
    print(num%2,end='')

decimaltobin(valu)'''

'''term = int(input("Enter total term"))
list=[]
for i in range(term):
    list.append(int(input("enter the values")))

s= 0
for v in list:
    s=s+v
print("sum ofthe value "+ str(s))
print("average of value "+str(s/term)) '''   


'''first=input("enter the first name : ")
last=input("enter the last name")

first1=first.upper()
last1=last.upper()

print("your first name and last name is "+str(first1)+" "+str(last1))'''

'''use = input("enter the bio ")
use1= use.split()
print("length of the string "+str(len(use1)))
if "the" in use1:
    print("the found ")'''

'''author_book={}
for i in range(5):
    author=input("Enter author name ")
    book = input("enter its author name")
    author_book[author]=book

print("last author is "+str(list(author_book.keys())[-1]))
print("last author is "+str(list(author_book.values())[-1]))'''

'''gb=float(input("enter memory in gb"))
#1gb = 1073741824 bytes
memory = 1073741824*gb
gb1=memory/1073741824
print("GB is converted to bytes "+str(memory))
print("bytes to Gb "+str(gb1))'''

'''name = input("Enter the name ")
f_name=input("Enter the father name ")
Cnic=input("enter the cnci number")
Age=input("enter the age ")
contact=input("enter the contact number ")
print("These are details of student")
print("Name       \t\t "+str(name))
print("Fathe Name \t\t "+str(f_name))
print("Cnic       \t\t "+str(Cnic))
print("Age        \t\t "+str(Age))
print("Contact    \t\t "+str(contact))

Cnic1=input("enter the cnic updated ")
Age1=input("enter the age ")
contact1=input("enter the contact ")
print("updated cnic "+str(Cnic1))
print("updated age "+str(Age1))
print("updated contact "+str(contact1))'''


'''lst=[]

for i in range(5):
    lst.append(input("enter the number "))
    print(lst)

def maximum(maxi):
    print(max(maxi))

maximum(lst)'''

'''def mark(marks):
    marks=input("enter the marks ")
    if marks==1100:
        print("free education")
    elif marks>=1000:
        print("80% Monthly Fees Deduction")
    elif marks>=900:
        print("60% Monthly Fees Deduction")
    elif marks>=800:
        print("40% Monthly Fees Deduction")
    elif marks>=700:
        print("30% Monthly Fees Deduction")
    elif marks>=600:
        print("There is No Scholarship")
    else:
        print("there is no admission for You")

print(mark(""))'''

'''def lengths(length):
    area=length*length
    perimeter=4*length
    print("area"+str(area))
    print("perimeter"+str(perimeter))
    square1=area**1/2
    square2=perimeter**1/2
    print("square root of area"+str(square1))
    print("square root perimeter"+str(square2))
    combine=square1+square2
    print("combine result "+str(combine))

l=float(input("enter the number"))
lengths(l)'''
    
net =







































