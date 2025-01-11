computer = ['ram','rom','ssd','mouse','key board']
for computers in computer:#This line tells Python to retrieve the first value from the list computer and store it in the variable computers.
    print(computers)

    computer = ['ram','rom','ssd','mouse','key board']
for computers in computer:
          print(computers.title()+"is the important part in computer")

for value1 in range(1,5):#The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide.
       print(value1)
numbers = list(range(1,6))
print(numbers)
even=list(range(2,20,1))
print(even)#the range() function starts with the value 2 and then adds 1 to that value. It adds 2 repeatedly until it reaches or passes the end value, 20.

squares=[]
for value2 in range(1,11):
     square=value2**2
     squares.append(square)
     print(squares)#We start with an empty list called squares at u. At v, we tell Python to loop through each value from 1 to 10 using the range() function. Inside the loop, the current value is raised to the second power and stored in the Working with Lists 63 variable square at w. At x, each new value of square is appended to the list squares. Finally, when the loop has finished running, the list of squares is printed at y


import wwl2