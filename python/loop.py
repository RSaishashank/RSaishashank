# loops i python
# 1 for loop
# 2 while loop
# iterable  datatypes:
# str list tuple dict set

#i = [10,20,30,40]
#for value in i:
 #   print(value)

#i = [10,20,30,40]
#sum = 10
#for value in i:
#    sum+=value
#    print(sum)

#for value in range(10):
 #   print(value)

#for value in range(5,10):
#    print(value)

#for value in range(15,100,10):
#    print(value)

#sum = 0
#for value in range(0,10):
#    sum+=value
#    print(sum)


#break
#continue
#enumerate

'''for value in range(10):
    print(value)'''

'''i = [10,20,30,40,50]
key = 45

for value in i:
    if value == key:
        print("element found")
        break
    else:
        continue
else:
    print("element not found")'''

'''i = [10,20,30,40,50]
key = 20

for index,value in enumerate(i):
    if value == key:
        print("element found at",index)
        break
    else:
        pass
        print("sha")
else:
    print("element not found")'''

#for index,value in enumerate(i):
#    print(index,value)

''''while [condition]:
    [statement]
else:'''''

'''shashank = 1
sum =0
while shashank <=20:
    sum+=shashank
    shashank+=1
    print(sum)
'''
'''
for value in range(1500,2701):
    if value%5==0 and value%7==0:
     print(value)
'''
'''for value in range(1,50):
    if value%2==0:
        print("even numbers",value)
    else:
        print("odd numbers",value)
'''
'''
for value in range(0,51):
    if value%3==0 and value%5==0:
        print("Fizzbuzz")   
    elif value%3==0:
        print("Fizz")
    elif value%5==0:
        print("Buzz")
    else:    
        print(value)'''
'''sum=0
for value in range(0,10):
     sum+=value
     print(sum)'''

'''def sum(n):
    n = (n-1)*n
    print(n)

for value in range(1,15):
    print(sum(value))
    

    print(sum(25))'''









    