computer = ['ram','rom','ssd','mouse','key board']
print(computer)
print(computer[0])
print(computer[2])
print(computer[-1])
print('ram is an imporatant device'+' '+computer[0].title())

computer.append('grahpic card') #appped to add to the last element
print(computer)
computer.insert(0,'graphic card') #insert is used to insert at a particular position
print(computer)
computer.remove('graphic card') #remove the element from the list
print(computer)
del computer[0] #delete an element at a particular place
print(computer)
print(computer.pop())#picks the  last element
print(computer.pop(1))#pops particular element
print(sorted(computer))#arranging alphabetical order in ascending
computer.sort(reverse=True)#arranging in alphabetical order in descending
print(computer)
computer.reverse()#arranging in reverse order
print(computer)
print(computer[-1])
s =["RACECAR"]
t =["CARRACE"]
s.sort(reverse=True)
print(s) 