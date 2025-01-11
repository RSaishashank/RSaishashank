'''l =[100,200,300,400,500,600]

i = iter(l)'''
#print(i)
#print(next(i))
      #or
'''for value in i:
    print(value)'''

import itertools

'''l1 = [10,20,30,40,50,60,70]
l2 = [100,200]
l3 = [200,400]

i = itertools.chain(l1,l2,l3) #using chain method we combined them

#print(next(i))

for value in i:
    print(value)'''

'''l =[10,20,30,40,50]
ds = 0
for value in itertools.cycle(l):#cycle provide infinity loop we have to give condition
    if ds < 20:
        print(value)
    else:
        break
    ds+=1 '''#we should make ds value or it goes to infinity loop


'''l =[10,20,30,40,50]
ds = 0
for value in itertools.repeat(l):#cycle provide infinity loop we have to give condition
    if ds < 20:
        print(value)
    else:
        break
    ds+=1''' 

#tee

'''l=[10,20,30,40,50,60]
i = iter(l)
t = itertools.tee(i)

for value in t[0]:
    print(value)
for value in t[1]:
    print(value)'''
    
'''l1 = [10,20,30,40,50,60,70]
l2 = [100,200]
l3 = [200,400]

i =itertools.chain(l1,l2,l3)
#print(i)

for value in itertools.islice(i,0,8): #used for slicing
    print(value)'''

'''count = 0
for value in itertools.count():
    if count >20:
        break
    else:
        print(value)
    count+=1'''

'''l = [1,2,3,4,5,6,7,8,9]
print(list(itertools.permutations(l,2))) #shows the number of combinations
print(list(itertools.combinations(l,2))) #shows the no of combinations
'''
